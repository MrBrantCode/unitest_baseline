"""
QUESTION:
Design a function `calculate_average_rating` that takes a `movie_id` as an argument and returns the average rating of the movie with the given `movie_id` from the 'Movies' table in the "movies.db" database. The function should connect to the SQLite database, execute a SQL query to calculate the average rating, and return the result. Ensure the function avoids SQL injection by using parameterized queries.
"""

import sqlite3

def calculate_average_rating(movie_id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    query = "SELECT AVG(Rating) FROM Movies WHERE Movie_ID = ?"
    cursor.execute(query, (movie_id,))
    result = cursor.fetchone()
    return result[0]