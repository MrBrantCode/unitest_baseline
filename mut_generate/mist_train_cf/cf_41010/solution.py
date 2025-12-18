"""
QUESTION:
Implement two functions, `user_user_cf` and `item_item_cf`, that perform collaborative filtering to generate movie recommendations based on user ratings. 

The `user_user_cf(user_ratings, movies_list)` function takes a 2D array `user_ratings` with shape (1, n) and a list of movie indices `movies_list` as input and returns a list of recommended movies using user-user collaborative filtering.

The `item_item_cf(user_ratings, movies_list)` function takes the same inputs and returns a list of recommended movies using item-item collaborative filtering. 

Assume that the `user_ratings` array has a shape of (1, n), where each column represents a movie and each row represents a user, and the `movies_list` contains the indices of the movies that the user has rated. 

Both functions should return a list of recommended movies based on the corresponding collaborative filtering method.
"""

import numpy as np

def entrance(user_ratings, movies_list):
    # Calculate user-user similarity matrix
    user_similarity = np.dot(user_ratings, user_ratings.T) / (np.linalg.norm(user_ratings) * np.linalg.norm(user_ratings.T))

    # Find the most similar user to the current user
    most_similar_user = np.argmax(user_similarity)

    # Get the ratings of the most similar user for unrated movies
    recommended_movies = [movie for movie in range(user_ratings.shape[1]) if movie not in movies_list]
    recommended_ratings = [user_ratings[0][movie] for movie in recommended_movies]

    return [recommended_movies[i] for i in np.argsort(recommended_ratings)[::-1]]

def entrance(user_ratings, movies_list):
    # Calculate item-item similarity matrix
    item_similarity = np.dot(user_ratings.T, user_ratings) / (np.linalg.norm(user_ratings.T) * np.linalg.norm(user_ratings))

    # Find the most similar movies to the rated movies
    most_similar_movies = [np.argmax(item_similarity[movie]) for movie in movies_list]

    # Get the unrated movies with the highest similarity to the rated movies
    recommended_movies = [movie for movie in range(user_ratings.shape[1]) if movie not in movies_list]
    recommended_ratings = [np.mean(item_similarity[movies_list, movie]) for movie in recommended_movies]

    return [recommended_movies[i] for i in np.argsort(recommended_ratings)[::-1]]