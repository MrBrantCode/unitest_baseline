"""
QUESTION:
Calculate the distance between each cyclist and every other cyclist using the great-circle distance formula. Assume that Earth is a perfect sphere and the city is located exactly at the equator. The cyclists are traveling in eight different directions: North, South, East, West, Northeast, Northwest, Southeast, and Southwest, at speeds of 20km/h, 18km/h, 16km/h, 14km/h, 22km/h, 24km/h, 26km/h, and 28km/h respectively. Implement a function called `calculate_cyclist_distances(T)` that takes time `T` (in hours) as input and returns a list of distances between each pair of cyclists and the average distance between the cyclists.
"""

def calculate_cyclist_distances(T):
    """
    Calculate the distance between each pair of cyclists and the average distance between the cyclists.

    Parameters:
    T (float): Time in hours.

    Returns:
    list: A list of distances between each pair of cyclists and the average distance between the cyclists.
    """
    
    # Define the Earth's radius in km
    R = 6371
    
    # Define the speeds for each direction in km/h
    speeds = [20, 18, 16, 14, 22, 24, 26, 28]
    diagonal_speeds = [speed / (2 ** 0.5) for speed in speeds[4:]]
    speeds = speeds[:4] + diagonal_speeds
    
    # Calculate the distances for directly opposite directions
    direct_distances = [2 * T, 2 * T, 2 * T, 2 * T]
    
    # Calculate the distances for diagonal directions
    diagonal_distances = [4 * T, 2 * (3 ** 0.5) * T, 4 * T, 2 * (3 ** 0.5) * T, 
                         4 * T, 2 * (3 ** 0.5) * T, 4 * T, 2 * (3 ** 0.5) * T, 
                         4 * T, 2 * (3 ** 0.5) * T, 4 * T, 2 * (3 ** 0.5) * T]
    
    # Combine the distances
    distances = direct_distances + diagonal_distances
    
    # Calculate the average distance
    average_distance = sum(distances) / len(distances)
    
    return distances + [average_distance]