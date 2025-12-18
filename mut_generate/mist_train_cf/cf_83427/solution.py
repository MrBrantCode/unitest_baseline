"""
QUESTION:
Write a function named `sort_movies` that takes a list of tuples, where each tuple contains a movie name and its release year, and returns the list sorted in reverse chronological order by release year.
"""

def sort_movies(movies):
    return sorted(movies, key=lambda movie: movie[1], reverse=True)