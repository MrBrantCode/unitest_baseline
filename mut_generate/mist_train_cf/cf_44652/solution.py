"""
QUESTION:
Write a function named `sort_movies` that takes a list of movie information as input, where each movie is represented as a tuple of (title, release year, director's name). The function should return the sorted list in descending order by release year, and for movies with the same release year, sort them in ascending order by the director's name.
"""

def sort_movies(movies):
    return sorted(movies, key=lambda movie: (-movie[1], movie[2]))