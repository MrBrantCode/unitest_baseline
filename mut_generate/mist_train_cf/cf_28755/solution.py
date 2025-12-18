"""
QUESTION:
Implement the following functions:

1. `select_year(data: dict, year: int) -> dict`: This function takes a dictionary containing movie data and a year as input, and returns a new dictionary containing only the movies from the specified year.

2. `find_nearest_movies(location: tuple, movies: dict) -> list`: This function takes a location's coordinates and a dictionary containing movie locations and their coordinates as input, and returns a list of 10 nearest movie locations along with their distances from the input location.

Note: The `coord_finder(location: str) -> tuple` function is assumed to be already implemented and available, as it is not part of the implementation task.
"""

def select_year(data: dict, year: int) -> dict:
    """
    Filters the movie data dictionary to include only movies from the specified year.
    
    Args:
    data (dict): A dictionary containing movie data.
    year (int): The year for which movies need to be selected.
    
    Returns:
    dict: A new dictionary containing only the movies from the specified year.
    """
    return {title: details for title, details in data.items() if details['year'] == year}

def entrance(location: tuple, movies: dict) -> list:
    """
    Finds the 10 nearest movie locations along with their distances from the input location.
    
    Args:
    location (tuple): The coordinates (latitude, longitude) of the input location.
    movies (dict): A dictionary containing movie locations and their coordinates.
    
    Returns:
    list: A list of 10 nearest movie locations along with their distances from the input location.
    """
    distances = {}
    for title, details in movies.items():
        movie_location = coord_finder(details['location'])
        distance = ((location[0] - movie_location[0])**2 + (location[1] - movie_location[1])**2)**0.5
        distances[title] = distance
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    return sorted_distances[:10]