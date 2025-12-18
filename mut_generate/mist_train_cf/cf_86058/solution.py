"""
QUESTION:
Create a function named `create_distance_matrix` that takes in a list of GPS coordinates and returns a matrix representing the shortest distances between these coordinates. The function should be able to handle a large number of coordinates and output the distances in a 2D matrix format. The matrix should be square, with the number of rows and columns equal to the number of input coordinates. The value at each index [i][j] should represent the shortest distance between the coordinates at index i and j.
"""

import math
from typing import List, Tuple

def create_distance_matrix(coordinates: List[Tuple[float, float]]) -> List[List[float]]:
    """
    This function calculates the shortest distances between a list of GPS coordinates.

    Args:
    coordinates (List[Tuple[float, float]]): A list of tuples, where each tuple contains a pair of GPS coordinates.

    Returns:
    List[List[float]]: A 2D matrix representing the shortest distances between the input coordinates.
    """

    # Initialize an empty matrix with zeros, with the same number of rows and columns as the number of input coordinates
    distance_matrix = [[0 for _ in range(len(coordinates))] for _ in range(len(coordinates))]

    # Iterate over each pair of coordinates
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            # If the coordinates are the same, the distance is 0
            if i == j:
                distance_matrix[i][j] = 0
            else:
                # Calculate the distance using the Haversine formula
                lat1, lon1 = math.radians(coordinates[i][0]), math.radians(coordinates[i][1])
                lat2, lon2 = math.radians(coordinates[j][0]), math.radians(coordinates[j][1])
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
                c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
                distance_matrix[i][j] = 6371 * c  # Radius of the Earth in kilometers

    return distance_matrix