"""
QUESTION:
Write a function `blue_cars_produced` that takes the number of white cars produced as input and returns the number of blue cars produced, given that 5 blue cars are produced for every 3 white cars.
"""

def blue_cars_produced(white_cars):
    """
    Returns the number of blue cars produced given the number of white cars produced.

    Args:
        white_cars (int): The number of white cars produced.

    Returns:
        int: The number of blue cars produced.
    """
    return (5/3) * white_cars