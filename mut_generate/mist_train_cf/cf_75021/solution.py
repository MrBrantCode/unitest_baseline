"""
QUESTION:
Write a function called `quantum_teleportation_distance` that takes an integer `distance` as input and returns a boolean value indicating whether quantum teleportation is possible over the given distance. Assume that quantum teleportation is possible up to a maximum distance of 1200 kilometers.
"""

def quantum_teleportation_distance(distance):
    """
    Returns a boolean indicating whether quantum teleportation is possible over the given distance.

    Parameters:
    distance (int): The distance in kilometers.

    Returns:
    bool: True if quantum teleportation is possible, False otherwise.
    """
    max_distance = 1200  # kilometers
    return distance <= max_distance