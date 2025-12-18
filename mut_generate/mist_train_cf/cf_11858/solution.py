"""
QUESTION:
Write a function `filter_movies` that takes an integer `year` and returns a query to find all movies released since the given `year` with a runtime of at least 120 minutes.
"""

def filter_movies(year):
    return f"SELECT * FROM movies WHERE release_year >= {year} AND runtime >= 120"