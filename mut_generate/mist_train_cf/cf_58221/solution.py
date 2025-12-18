"""
QUESTION:
Write a function `calculate_floors` that calculates the number of floors in a building given its total height. Each floor is 14.3 feet. The function should return the number of floors rounded to the nearest whole number, as a building cannot have a fraction of a floor.
"""

def calculate_floors(total_height):
    """
    Calculate the number of floors in a building given its total height.
    
    Each floor is 14.3 feet. The function returns the number of floors 
    rounded to the nearest whole number.

    Args:
        total_height (float): The total height of the building in feet.

    Returns:
        int: The number of floors in the building.
    """
    floor_height = 14.3
    return round(total_height / floor_height)