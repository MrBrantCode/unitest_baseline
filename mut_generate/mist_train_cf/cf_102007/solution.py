"""
QUESTION:
Create a function `convert_x_to_y` that takes an integer `x` as input and returns an integer `y` based on the following conditions: 
- if `x` is less than 1, return 0
- if `x` is between 1 and 10 (inclusive), return `x * 10`
- if `x` is between 11 and 20 (inclusive), return `x + 10`
- if `x` is between 21 and 30 (inclusive), return `x - 10`
- if `x` is greater than 30, return -1.
"""

def convert_x_to_y(x):
    if x < 1:
        return 0
    elif 1 <= x <= 10:
        return x * 10
    elif 11 <= x <= 20:
        return x + 10
    elif 21 <= x <= 30:
        return x - 10
    else:
        return -1