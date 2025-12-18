"""
QUESTION:
Create a function `sort_and_filter_movies` that sorts a list of movies by release year and filters out movies with a budget less than $5 million. The function should take a list of dictionaries, where each dictionary represents a movie with the keys "title", "year", "country", and "budget". The function should return a list of movies sorted by release year and only include movies with a budget of at least $5 million.
"""

def sort_and_filter_movies(movies):
    # Filter movies with budget of at least $5 million
    movies = list(filter(lambda x: x.get("budget", 0) >= 5000000, movies))
    # Sort movies by release date
    movies.sort(key=lambda x: x["year"])
    return movies