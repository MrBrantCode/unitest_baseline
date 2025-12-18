"""
QUESTION:
Write a function `top_movies` that takes a list of dictionaries, where each dictionary contains a movie title and its rating, and returns the titles of the top 10 movies with the highest ratings. The titles should be sorted in descending order based on their ratings. If two movies have the same rating, prioritize the movie with the lower alphabetical title.
"""

def top_movies(movies):
    """
    Returns the titles of the top 10 movies with the highest ratings.

    Args:
        movies (list): A list of dictionaries, where each dictionary contains a movie title and its rating.

    Returns:
        list: The titles of the top 10 movies, sorted in descending order based on their ratings.
    """
    # Sort the movie objects in descending order based on ratings
    sorted_movies = sorted(movies, key=lambda x: (-x["rating"], x["title"]))
    
    # Return the titles of the top 10 movies
    return [movie["title"] for movie in sorted_movies[:10]]