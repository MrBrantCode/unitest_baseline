"""
QUESTION:
Write a function `convert` that takes a unit and a distance as input, and returns the converted distance in the opposite unit (either kilometers to miles or miles to kilometers). The function should only accept non-negative distances and valid units ("km" or "mi"). If the input is invalid, the function should return `None`.
"""

def convert(unit, distance):
    """
    This function converts a distance from one unit to another.
    
    Parameters:
    unit (str): The unit of the input distance. It can be either "km" or "mi".
    distance (float): The distance to be converted.
    
    Returns:
    float or None: The converted distance if the input is valid, otherwise None.
    """
    if (unit.lower() == "km" and distance >= 0):
        return distance * 0.621371
    elif (unit.lower() == "mi" and distance >= 0):
        return distance * 1.60934
    else:
        return None