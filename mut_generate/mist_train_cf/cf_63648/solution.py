"""
QUESTION:
Write a function `sort_movies` that sorts a list of movies by release year in descending order, and in cases of a tie, by box office grossing in descending order. The input is a list of tuples where each tuple contains the movie title, release year, and box office grossing.
"""

def sort_movies(movies):
    return sorted(movies, key=lambda movie: (-movie[1], -movie[2]))