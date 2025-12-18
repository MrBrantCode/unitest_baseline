"""
QUESTION:
Implement a function `polynomial_kernel(x, y, d, c)` that calculates the dot product of two vectors `x` and `y` using the polynomial kernel trick, where `d` is the degree of the polynomial and `c` is a constant. The polynomial kernel function is defined as K(x,y) = (x·y + c)^d. 

The function should take four arguments: two vectors `x` and `y`, and two scalars `d` and `c`. The vectors `x` and `y` should be one-dimensional, and the scalars `d` and `c` should be integers. 

For example, given `x=2`, `y=3`, `d=2`, and `c=0`, the function should return `36` because `(2*3+0)^2 = 36`.
"""

def polynomial_kernel(x, y, d, c):
    """
    This function calculates the dot product of two vectors x and y using the polynomial kernel trick.

    Parameters:
    x (float): The first vector.
    y (float): The second vector.
    d (int): The degree of the polynomial.
    c (int): A constant.

    Returns:
    float: The dot product of x and y using the polynomial kernel trick.
    """
    return (x * y + c) ** d