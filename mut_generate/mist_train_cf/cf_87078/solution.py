"""
QUESTION:
Write a function named `multiply` that takes two non-negative integers `x` and `y` as input and returns their product without using the multiplication operator (*) or any built-in multiplication functions, loops, or recursion, and with a time complexity of O(log n), where n is the maximum value between `x` and `y`.
"""

def multiply(x, y):
    # Base cases
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    
    # Recursive calls
    x_half = x >> 1  # Divide x by 2
    y_double = y << 1  # Multiply y by 2
    
    # Recursive multiplication
    result = multiply(x_half, y_double)
    
    # Adjust result for odd values of x
    if x % 2 == 1:
        result += y
    
    return result