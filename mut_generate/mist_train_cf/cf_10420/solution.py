"""
QUESTION:
Create a function that allows users to rate a movie from 1 to 5 stars if they have added it to their favorites list. 

The function should take two parameters: a user ID and a movie ID. It should return True if the rating was successful and False if the user has not added the movie to their favorites.
"""

def rate_movie(user_id, movie_id, favorites, ratings):
    if movie_id in favorites.get(user_id, []):
        ratings[user_id] = ratings.get(user_id, {})
        ratings[user_id][movie_id] = ratings[user_id].get(movie_id, 0)
        return True
    else:
        return False