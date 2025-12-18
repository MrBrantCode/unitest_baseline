"""
QUESTION:
Create a function `double_value` that takes one argument `number`. The function should return the input number doubled if the input is an integer or a floating-point number. If the input is neither an integer nor a floating-point number, the function should return "Invalid input".
"""

def double_value(number):
    """
    Returns the input number doubled if it's an integer or a float, otherwise returns "Invalid input".
    
    Parameters:
    number (int or float): The input number to be doubled.
    
    Returns:
    int or float or str: The doubled number or "Invalid input".
    """
    if isinstance(number, (int, float)):
        return number * 2
    else:
        return "Invalid input"