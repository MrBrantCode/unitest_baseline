"""
QUESTION:
Write a function `calculate_total_distance` that calculates the total distance covered by Gabriella in all four shows given the distances covered in each show. The function should take a list of distances as input and return the total distance. Assume that the input list will contain only positive float numbers representing the distances in meters.
"""

def calculate_total_distance(distances):
    """
    Calculate the total distance covered by Gabriella in all four shows.

    Args:
        distances (list): A list of distances in meters.

    Returns:
        float: The total distance covered by Gabriella.
    """
    return sum(distances)