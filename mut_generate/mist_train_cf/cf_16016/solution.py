"""
QUESTION:
Implement a function `multiply(x, y)` that takes two integers `x` and `y` as input and returns their product without using the multiplication operator. The function should handle cases where `x` or `y` is negative or zero, and should have a time complexity of O(log y).
"""

def multiply(x, y):
    """
    This function multiplies two integers x and y without using the multiplication operator.
    
    The function uses bitwise operations and recursion to achieve the multiplication. 
    It handles cases where x or y is negative or zero and has a time complexity of O(log y).
    
    Parameters:
    x (int): The first integer.
    y (int): The second integer.
    
    Returns:
    int: The product of x and y.
    """
    # Base case: if y is 0, the product is 0
    if y == 0:
        return 0
    
    # If y is negative, convert the problem to a positive y and remember the sign
    if y < 0:
        return -multiply(x, -y)
    
    # If x is negative, convert the problem to a positive x and remember the sign
    if x < 0:
        return -multiply(-x, y)
    
    # Recursive case: x + x * (y - 1)
    if y % 2 == 0:
        # If y is even, divide the problem into two smaller sub-problems of size y // 2
        half_product = multiply(x, y // 2)
        return half_product + half_product
    else:
        # If y is odd, divide the problem into two smaller sub-problems of size (y - 1) // 2
        half_product = multiply(x, (y - 1) // 2)
        return x + half_product + half_product