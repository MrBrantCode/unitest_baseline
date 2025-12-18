"""
QUESTION:
Write a function `travelling_salesman` that takes a 2D list of distances between cities as input and returns the minimum total distance and the corresponding order of cities to visit. The function should consider all possible routes and find the one with the shortest total distance. The input list is a square matrix where distances[i][j] is the distance from city i to city j.
"""

import itertools

def travelling_salesman(distances):
    """
    This function calculates the minimum total distance and the corresponding order of cities to visit.
    
    Parameters:
    distances (list): A 2D list of distances between cities.
    
    Returns:
    tuple: A tuple containing the minimum total distance and the corresponding order of cities to visit.
    """
    # Create a list of indices which represents cities
    cities = list(range(len(distances)))
    
    # Iterate over all possibilities of orders (sequences of visited cities)
    routes = list(itertools.permutations(cities))
    
    # Initiate minimum distance to a high value
    min_distance = float('inf')
    min_route = None
    
    # For each route 
    for route in routes:
        # Sum the distances for the route
        sum_route = sum(distances[route[i-1]][route[i]] for i in range(len(route)))
        # If the distance is less than any found before, save it
        if sum_route < min_distance:
            min_distance = sum_route
            min_route = route
            
    return min_distance, min_route