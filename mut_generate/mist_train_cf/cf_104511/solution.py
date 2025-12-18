"""
QUESTION:
Write a function `filter_movies` that takes no arguments, but uses the variable `year` and returns a SQL query string. The query should select all columns from a table named `movies` where the `release_year` is greater than a given `year`, the `runtime` is 120 minutes or more, and the `rating` is 7.5 or higher.
"""

def filter_movies(year):
    return f"SELECT * FROM movies WHERE release_year > {year} AND runtime >= 120 AND rating >= 7.5;"