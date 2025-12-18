"""
QUESTION:
Write a function named `add_with_conversion` that takes two parameters, `x` and `y`, where `x` is an integer and `y` is a string representing an integer. Add `x` and `y` together and return the result as a floating-point number with 2 decimal places. The function must convert `y` to an integer before performing the addition. The function should not change the data type of `x`.
"""

def add_with_conversion(x, y):
    """
    Adds an integer x and a string y (representing an integer) together and returns the result as a floating-point number with 2 decimal places.

    Args:
        x (int): The integer to add.
        y (str): A string representing an integer to add.

    Returns:
        float: The sum of x and y as a floating-point number with 2 decimal places.
    """
    # Convert y to an integer
    y = int(y)
    
    # Add x and the converted value of y
    sum_value = x + y
    
    # Return the sum as a floating-point number with 2 decimal places
    return round(sum_value, 2)