"""
QUESTION:
Write a function `multiply_x_y` that takes an integer `x` and a string `y` as input. The function should return the result of the multiplication of `x` and `y`. The function should handle both cases where the intention is to repeat the string `y` for `x` number of times and where the intention is to calculate the numerical multiplication of `x` and `y` (assuming `y` is a string representation of an integer). The function should return the result as either a string or an integer depending on the case.
"""

def multiply_x_y(x, y):
    """
    This function takes an integer x and a string y as input.
    It returns the result of the multiplication of x and y.
    The function handles both cases where the intention is to repeat the string y for x number of times 
    and where the intention is to calculate the numerical multiplication of x and y 
    (assuming y is a string representation of an integer).
    
    Parameters:
    x (int): The multiplier.
    y (str): The multiplicand.
    
    Returns:
    str or int: The result of the multiplication.
    """
    if y.isdigit():
        # If y is a string representation of an integer, perform numerical multiplication
        return x * int(y)
    else:
        # If y is a string, repeat it x times
        return x * y