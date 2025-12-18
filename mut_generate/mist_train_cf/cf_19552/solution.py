"""
QUESTION:
Write a function nearest_neighbor_tsp that implements the Nearest Neighbor algorithm to find an approximate solution to the Traveling Salesman Problem (TSP). The function should take as input a 2D list distance_matrix representing the distances between cities and return a list of city indices representing the tour. The function should have a time complexity of O(n^2), where n is the number of cities.
"""

def nearest_neighbor_tsp(distance_matrix):
    """
    This function implements the Nearest Neighbor algorithm to find an approximate solution to the Traveling Salesman Problem (TSP).
    
    Args:
        distance_matrix (2D list): A 2D list representing the distances between cities.
    
    Returns:
        list: A list of city indices representing the tour.
    """
    
    # Initialize the starting city as the first city in the distance matrix
    start_city = 0
    
    # Create a list to store the tour
    tour = [start_city]
    
    # Create a set of unvisited cities
    unvisited_cities = set(range(len(distance_matrix)))
    unvisited_cities.remove(start_city)
    
    # Initialize the current city
    current_city = start_city
    
    # Repeat the following steps until all cities are visited
    while unvisited_cities:
        # Find the nearest unvisited city from the current city
        nearest_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        
        # Add the nearest city to the tour
        tour.append(nearest_city)
        
        # Mark the nearest city as visited
        unvisited_cities.remove(nearest_city)
        
        # Set the nearest city as the current city
        current_city = nearest_city
    
    # Add the starting city to the tour to complete the loop
    tour.append(start_city)
    
    return tour