"""
QUESTION:
Write a function called `sort_movies` that takes a list of tuples as an argument, where each tuple contains a film name and its release year. The function should return the list of films sorted in reverse chronological order. The function should not modify the original list.
"""

def sort_movies(movie_list):
    return sorted(movie_list, key=lambda x: x[1], reverse=True)