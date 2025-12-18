"""
QUESTION:
Implement a function `calculate_multiverse_dimensions` that calculates the total number of dimensions in a multiverse, given the number of universes and dimensions per universe. The function should take two parameters: `universes` (the number of universes) and `dimensions_per_universe` (the number of dimensions per universe). The function should return the total number of dimensions in the multiverse.
"""

def calculate_multiverse_dimensions(universes, dimensions_per_universe):
    """
    Calculate the total number of dimensions in a multiverse.

    Args:
        universes (int): The number of universes in the multiverse.
        dimensions_per_universe (int): The number of dimensions per universe.

    Returns:
        int: The total number of dimensions in the multiverse.
    """
    return universes * dimensions_per_universe