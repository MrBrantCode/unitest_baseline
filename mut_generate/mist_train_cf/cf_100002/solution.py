"""
QUESTION:
Create a function named `sort_movies_by_release_date` that takes a list of dictionaries representing movies, where each dictionary contains the keys 'title', 'year', 'country', and 'budget'. The function should filter out movies with a budget of less than $5 million, sort the remaining movies by release date in ascending order, and return the sorted list.
"""

def sort_movies_by_release_date(movies):
    # Filter movies with budget of at least $5 million
    movies = list(filter(lambda x: x["budget"] >= 5000000, movies))
    # Sort movies by release date
    movies.sort(key=lambda x: x["year"])
    return movies