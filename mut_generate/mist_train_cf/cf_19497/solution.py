"""
QUESTION:
Create a function `filter_movies` that takes a 2D list of movie ratings as input, where each inner list contains a movie title and its corresponding rating. The function should return a list of movie titles with ratings between 8 and 9 (inclusive), sorted in alphabetical order.
"""

def filter_movies(movie_ratings):
    """
    Filter movies with ratings between 8 and 9 (inclusive) and return their titles in alphabetical order.

    Args:
        movie_ratings (list): A 2D list of movie ratings, where each inner list contains a movie title and its corresponding rating.

    Returns:
        list: A list of movie titles with ratings between 8 and 9 (inclusive), sorted in alphabetical order.
    """
    return sorted([movie[0] for movie in movie_ratings if 8 <= movie[1] <= 9])