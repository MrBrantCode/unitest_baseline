"""
QUESTION:
Implement a function `nearest_neighbor_tsp` that takes as input a 2D list `distance_matrix` representing the distances between cities, where `distance_matrix[i][j]` is the distance from city `i` to city `j`. The function should return a list of city indices representing the order in which the cities should be visited to solve the Traveling Salesman Problem using the Nearest Neighbor Algorithm, and the total distance of the tour. The function should start at an arbitrary city and return to the starting city to complete the tour.
"""

def nearest_neighbor_tsp(distance_matrix):
    """
    This function solves the Traveling Salesman Problem using the Nearest Neighbor Algorithm.
    
    Args:
    distance_matrix (list): A 2D list representing the distances between cities.
    
    Returns:
    list: A list of city indices representing the order in which the cities should be visited.
    int: The total distance of the tour.
    """
    
    # Initialize the starting city as 0 and mark it as visited
    current_city = 0
    visited = [False] * len(distance_matrix)
    visited[current_city] = True
    
    # Create an empty list to store the tour
    tour = [current_city]
    
    # While there are unvisited cities
    while False in visited:
        # Find the nearest unvisited city to the current city
        min_distance = float('inf')
        next_city = None
        for i in range(len(distance_matrix)):
            if not visited[i] and distance_matrix[current_city][i] < min_distance:
                min_distance = distance_matrix[current_city][i]
                next_city = i
        
        # Add the nearest city to the tour
        tour.append(next_city)
        
        # Mark the nearest city as visited
        visited[next_city] = True
        
        # Update the current city to be the nearest city
        current_city = next_city
    
    # Return to the starting city to complete the tour
    tour.append(tour[0])
    
    # Calculate the total distance of the tour
    total_distance = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    
    return tour, total_distance