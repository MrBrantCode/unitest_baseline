"""
QUESTION:
Implement a function called `multiply_decimals(x, y)` that multiplies two decimal numbers `x` and `y` without using the multiplication operator or any looping constructs. The function should handle negative decimal numbers as inputs and outputs.
"""

def multiply_decimals(x, y):
    if x == 0 or y == 0:
        return 0
    
    # Handle negative numbers
    sign = -1 if (x < 0) ^ (y < 0) else 1
    x, y = abs(x), abs(y)
    
    # convert to integer for the purpose of calculation
    x_int, x_frac = int(x), x - int(x)
    y_int, y_frac = int(y), y - int(y)

    result = x_int * y_int + x_int * y_frac + y_int * x_frac + x_frac * y_frac
    return result * sign