# Item Based Collaborative Recommendation System

<p align="center">
	<img src="https://github.com/Aerospacerr/Item-Based-Collaborative-Filtering-Item-Item-Filtering-/blob/ef9199b44caf8095727b1cc7d3f53e6691aa533f/recommenders_systems.png" />

</p>

## Table of contents
* [General info](#general-info)
* [Project info](#project-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Developments](#developments)

## General info
Recommendation systems have been around us for quite some time now. Youtube, Facebook, Amazon, and many others provide some sort of recommendations to their users.   

Here, we explore the relationship between the pair of items (the user who bought Y, also bought Z). We find the missing rating with the help of the ratings given to the other items by the user.   

It was first invented and used by Amazon in 1998. Rather than matching the user to similar customers, item-to-item collaborative filtering matches each of the user’s purchased and rated items to similar items, then combines those similar items into a recommendation list.

## Project info
Here,we tried to create our own movie database with ratings by using "movies.csv" and "ratings.csv"(link down below)  
We calculated a suggestion with calculating the correlation between the entered movie and other movies. Hence we suggest a movie for user by using correlations among them.

## Technologies
Project is created with:
* PyCharm: 2021.3 
* Pandas: 1.3.4 (especially "corrwith")


	
## Setup
To run this project, just run the functions at the bottom of code and call "item_based_recommender". That's it!

## Developments 
It can be achieved more precise results merging both item-based and user-based recommendation by calculating "Weighted Average Recommendation Score". It will be developed on next project that I will do. It can become more likely a recommendation system like Netflix uses. For now, it is just simple version of item-based recommendation system



