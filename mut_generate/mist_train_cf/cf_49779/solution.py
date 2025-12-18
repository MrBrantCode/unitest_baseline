"""
QUESTION:
Design a function called `adjust_temperature` that takes in the current temperature and a desired temperature change as input and returns the new temperature. The function should be able to handle both positive (increase) and negative (decrease) temperature changes.
"""

def adjust_temperature(current_temp, temp_change):
    """
    Adjusts the current temperature by a specified temperature change.

    Args:
    current_temp (float): The current temperature.
    temp_change (float): The desired temperature change.

    Returns:
    float: The new temperature after adjustment.
    """
    return current_temp + temp_change