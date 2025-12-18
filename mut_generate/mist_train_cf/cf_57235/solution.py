"""
QUESTION:
Given a standard deviation value calculated from percentage values, determine the correct interpretation of the result. The standard deviation is calculated using the STDEV function and returns a decimal value. Write a function `interpret_standard_deviation` that takes this decimal value as input and returns the correct interpretation as a percentage value. The function should multiply the input by 100 to convert it to a percentage.
"""

def interpret_standard_deviation(std_dev):
    """
    This function takes a standard deviation value calculated from percentage values
    and returns its correct interpretation as a percentage value.

    Args:
        std_dev (float): The standard deviation value.

    Returns:
        float: The standard deviation as a percentage value.
    """
    return std_dev * 100