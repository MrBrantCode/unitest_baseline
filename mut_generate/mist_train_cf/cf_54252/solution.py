"""
QUESTION:
Develop a function named `multiply` that takes two integers `x` and `y` as input and returns their product without using standard multiplication operators. The function should also handle cases where either `x` or `y` is negative.
"""

def multiply(x, y):
    # Initialize result to 0
    result = 0

    # Handle the negative numbers case
    if y < 0:
        y, x = -y, -x

    # Loop through the range from 0 to absolute value of y
    for _ in range(abs(y)):
        result += x

    return result if x >= 0 else -result