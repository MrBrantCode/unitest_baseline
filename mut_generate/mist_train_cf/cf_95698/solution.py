"""
QUESTION:
Write a function `filter_movies` that takes a list of movie ratings as input, where each rating is a list containing a movie title and a numerical rating. The function should return a list of movie titles with ratings between 8 and 9 (inclusive), sorted alphabetically.
"""

def filter_movies(movie_ratings):
    """
    This function filters a list of movie ratings and returns a list of movie titles with ratings between 8 and 9 (inclusive), sorted alphabetically.

    Args:
        movie_ratings (list): A list of movie ratings, where each rating is a list containing a movie title and a numerical rating.

    Returns:
        list: A list of movie titles with ratings between 8 and 9 (inclusive), sorted alphabetically.
    """

    # Create a list to store movie titles
    selected_movies = [movie[0] for movie in movie_ratings if 8 <= movie[1] <= 9]

    # Sort the selected_movies list alphabetically
    selected_movies.sort()

    return selected_movies