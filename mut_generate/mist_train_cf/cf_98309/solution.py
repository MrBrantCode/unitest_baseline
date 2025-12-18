"""
QUESTION:
Create a function `solution_y` that takes an integer `x` as an argument and returns the integer `y` between 0 and 20 that satisfies the equation 4x - 7y + 9 = 0.
"""

def solution_y(x):
    y = (4*x + 9) / 7
    if y.is_integer() and 0 <= y <= 20:
        return int(y)
    else:
        return None