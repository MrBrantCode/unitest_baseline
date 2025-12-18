"""
QUESTION:
Create a function `units_of_measure` that takes a numerical value and a unit as input and returns the numerical value with the unit. The function should work with any numerical type, including integers and floating point values, and should be able to handle various units such as meters, seconds, etc. The function should be implemented in a way that allows for compile-time checking of unit consistency, preventing incorrect unit operations at runtime.
"""

def units_of_measure(value, unit):
    """
    Returns a string representation of a numerical value with a unit.

    Args:
        value (int or float): The numerical value.
        unit (str): The unit of the value.

    Returns:
        str: A string representation of the value with the unit.
    """
    return f"{value} {unit}"