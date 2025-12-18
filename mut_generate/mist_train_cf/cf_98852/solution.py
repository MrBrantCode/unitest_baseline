"""
QUESTION:
Write a function `average_release_year` that takes a list of movie dictionaries as input, where each dictionary contains a 'release_year' key. The function should return the average release year of all the movies.
"""

def average_release_year(movies):
    total_years = 0
    for movie in movies:
        total_years += movie['release_year']
    return total_years / len(movies)