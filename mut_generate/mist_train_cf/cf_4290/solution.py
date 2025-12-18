"""
QUESTION:
Write a function `filter_movies` that returns movies released since a given year, with a runtime of at least 120 minutes, and a rating of at least 7.5 out of 10. The results should be sorted in descending order based on the movie's rating.
"""

def filter_movies(movies, given_year):
    return sorted([movie for movie in movies if movie['release_year'] > given_year and movie['runtime'] >= 120 and movie['rating'] >= 7.5], key=lambda x: x['rating'], reverse=True)