"""
QUESTION:
Compose a SQL query for the function `find_top_movies` to retrieve the titles of the top 10 action movies from the 'movies' table, released in 2021, with revenue over $2,000,000 and a rating above 8.0, sorted by revenue in descending order. The 'movies' table contains the columns: title, release_year, revenue, rating, and genre.
"""

def find_top_movies(movies):
    query = """
    SELECT title 
    FROM movies
    WHERE release_year = 2021
      AND revenue > 2000000
      AND rating > 8.0
      AND genre = 'action'
    ORDER BY revenue DESC
    LIMIT 10
    """
    return query