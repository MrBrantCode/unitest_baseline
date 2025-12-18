"""
QUESTION:
Create a function `sort_movies` that takes a list of movies where each movie is a tuple of (title, release year, genre, runtime). The function should sort the movies by release year and return the movies with a runtime of at least 90 minutes, including their title, release year, genre, and runtime.
"""

def sort_movies(movies):
    """
    Sorts the movies by release year and returns the movies with a runtime of at least 90 minutes.

    Args:
        movies (list): A list of movies where each movie is a tuple of (title, release year, genre, runtime)

    Returns:
        list: A list of movies with a runtime of at least 90 minutes, sorted by release year
    """
    # Sort movies by release date
    movies = sorted(movies, key=lambda x: x[1])
    # Filter movies with runtime of at least 90 minutes
    return [(movie[0], movie[1], movie[2], movie[3]) for movie in movies if movie[3] >= 90]