"""
QUESTION:
Write a Python function named `calculate_total_distance` to calculate the total distance the birds have traveled. The function should take a list of distances as input, where each distance represents the distance traveled by the birds in a day. The function should return the total distance traveled by the birds.
"""

def calculate_total_distance(distances):
    """
    Calculate the total distance traveled by birds.

    Args:
        distances (list): A list of distances representing the distance traveled by the birds in each day.

    Returns:
        int: The total distance traveled by the birds.
    """
    return sum(distances)