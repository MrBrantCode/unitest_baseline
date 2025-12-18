"""
QUESTION:
Create a function named `multiply_decimals(x, y)` that multiplies two decimal numbers `x` and `y` without using the multiplication operator and without using any looping constructs or built-in functions that directly perform multiplication. The function should handle negative decimal numbers as inputs and outputs.
"""

def multiply_decimals(x, y):
    if x == 0 or y == 0:
        return 0
    
    # Handle negative numbers
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)
    
    result = 0
    while y > 0:
        result += x
        y -= 1
    
    return result * sign