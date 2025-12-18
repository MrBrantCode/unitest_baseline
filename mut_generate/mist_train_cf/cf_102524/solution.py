"""
QUESTION:
Create a function `scale_number` that takes in two parameters: `number` and `factor`, where `number` is an integer or float and `factor` is a float. The function should return the result of multiplying `number` by `factor` and then rounding it to the nearest integer without using built-in rounding functions. The output should be an integer. Both `number` and `factor` can be any real numbers, and the function should handle large numbers and extreme values efficiently.
"""

def scale_number(number, factor):
    """
    This function scales a given number by a certain factor and rounds it to the nearest integer.
    
    Args:
        number (int or float): The number to be scaled.
        factor (float): The factor by which the number is scaled.
    
    Returns:
        int: The scaled number rounded to the nearest integer.
    """
    scaled_number = number * factor
    return int(scaled_number + 0.5)