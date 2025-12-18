"""
QUESTION:
Write a function `tsp_brute_force` that solves the Traveling Salesman Problem (TSP) using a brute-force approach. The function should take a list of cities and their pairwise distances as input and return the shortest possible tour that visits each city exactly once and returns to the origin city.
"""

def tsp_brute_force(distances):
    """
    Solves the Traveling Salesman Problem (TSP) using a brute-force approach.

    Args:
    distances (list of lists): A 2D list where distances[i][j] is the distance between city i and city j.

    Returns:
    tuple: A tuple containing the shortest tour and its total distance.
    """
    
    # Get the number of cities
    num_cities = len(distances)
    
    # Initialize the shortest tour and its distance
    shortest_tour = None
    shortest_distance = float('inf')
    
    # Generate all permutations of cities
    import itertools
    for tour in itertools.permutations(range(num_cities)):
        # Calculate the total distance for the current tour
        distance = sum(distances[tour[i-1]][tour[i]] for i in range(num_cities))
        
        # Update the shortest tour if the current tour is shorter
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_tour = tour
    
    # Add the origin city to the end of the shortest tour to complete the cycle
    shortest_tour = shortest_tour + (shortest_tour[0],)
    
    return shortest_tour, shortest_distance