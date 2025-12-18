"""
QUESTION:
Create a function `get_top_movies` that takes a list of movie objects as input, where each movie object contains the movie's title, rating (out of 10), and number of votes. The function should return a list of the top 10 movies that have at least 100,000 votes and a rating above 8.0, ordered by their rating in descending order.
"""

def get_top_movies(movies):
    """
    Returns a list of the top 10 movies that have at least 100,000 votes and a rating above 8.0,
    ordered by their rating in descending order.

    Args:
        movies (list): A list of movie objects, each containing 'title', 'rating', and 'votes'.

    Returns:
        list: A list of the top 10 movies that meet the specified criteria.
    """
    # Filter movies that meet the criteria
    filtered_movies = [movie for movie in movies if movie['votes'] >= 100000 and movie['rating'] > 8.0]
    
    # Sort the filtered movies by rating in descending order
    sorted_movies = sorted(filtered_movies, key=lambda x: x['rating'], reverse=True)
    
    # Return the top 10 movies
    return sorted_movies[:10]