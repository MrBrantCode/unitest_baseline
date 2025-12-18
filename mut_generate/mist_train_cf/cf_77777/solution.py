"""
QUESTION:
Develop a function `multiplication(x, y)` to return the product of two n-digit integers `x` and `y` without using built-in multiplication, division, or modulo operators. The function should handle edge cases where `x` or `y` is 0 or negative.
"""

def multiplication(x, y):
    # Initialize the product to 0
    product = 0
    
    # Check if x or y is 0, return 0 if either is found
    if x == 0 or y == 0:
        return 0
    
    # If x is negative, flip the sign of y and make x positive
    if x < 0:
        x, y = -x, -y

    # Add x to product y times
    for _ in range(y):
        product += x

    # Return the product
    return product