###########################################
# Item-Based Collaborative Filtering (Item-Item Filtering)
###########################################
# Memory-Based Collaborative Filtering: Item Filtering

# Adım 1: Veri Setinin Hazırlanması
# Adım 2: User Movie Df'inin Oluşturulması
# Adım 3: Item-Based Film Önerilerinin Yapılması
# Adım 4: İşlemlerin Fonksiyonlaştırılması

# https://grouplens.org/datasets/movielens/

######################################
# Preparation of Dataset
######################################

import pandas as pd
pd.set_option('display.max_columns', 20)

#movie.csv is 27278x3
movie = pd.read_csv('/content/movie.csv')
#rating.csv is 14191605x4
rating = pd.read_csv('/content/rating.csv')

#we need to merge them by movieId to match ratings and movies
#df will be our merged main database
df = movie.merge(rating, how="left", on="movieId")


######################################
# Creating User_movie_df
######################################
#Firstly, let's examine our merged database
df.head()
df.shape

#look for unique titles to learn how many movies we have in df
df["title"].nunique()

#here are the top 5 movies that rated by users
df["title"].value_counts().head()

#we define rating_counts as we know the total number of rates to movies
rating_counts = pd.DataFrame(df["title"].value_counts())

#we drop least rated movies, here we say at least 1000 ratings
#name the selected movies as common_movies
rare_movies = rating_counts[rating_counts["title"] <= 1000].index
common_movies = df[~df["title"].isin(rare_movies)]
common_movies.shape
common_movies["title"].nunique() #we have 2544 movies left

#we will have movie names as columns and userID as rows
user_movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")

#let's see if it is like what we want
user_movie_df.shape #(97985, 2544)
user_movie_df.columns # movie names
user_movie_df.head(10)



######################################
# Adım 3: Item-Based Film Önerilerinin Yapılması
######################################
#Now we can calculated a suggestion with calculating the correlation
#for example let's pick Matrix
movie_name = "Matrix, The (1999)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


#Now we can pick a randomly movie
movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
movie_name = user_movie_df[movie_name]
user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)



######################################
# Let's sum all up and write with functions for different variables
######################################
import pandas as pd 

def create_movie_df(nr_drop_movie):
  #change these paths with your own path of database
    movie = pd.read_csv('/content/movie.csv')
    rating = pd.read_csv('/content/rating.csv')
    #merge datasets
    df = movie.merge(rating, how="left", on="movieId")
    rating_count = pd.DataFrame(df["title"].value_counts())
  #nr_drop_movies= number of dropped movies from list
    rare_movies = rating_count[rating_count["title"] <= nr_drop_movie].index
    common_movies = df[~df["title"].isin(rare_movies)]
    movie_df = common_movies.pivot_table(index=["userId"], columns=["title"], values="rating")
    return movie_df

def item_based_recommender(movie_name, movie_df):
    movie_name = user_movie_df[movie_name]
    return user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10)


movie_df = create_movie_df(nr_drop_movie=1000)

#example for Sherlock Holmes
item_based_recommender("Sherlock Holmes (2009)", movie_df)

#for randomly picked movie
movie_name = pd.Series(movie_df.columns).sample(1).values[0]
item_based_recommender(movie_name, movie_df)
