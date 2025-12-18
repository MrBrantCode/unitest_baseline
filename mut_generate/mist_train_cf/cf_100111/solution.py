"""
QUESTION:
Create a function called `solution_y` that accepts an integer `x` as input and returns an integer `y` that satisfies the equation `4x-7y+9=0`. The function should consider all possible integer values of `y` within the range of 0 to 20, inclusive, and return the correct solution.
"""

def solution_y(x):
    y = (4*x+9)/7
    if y.is_integer() and 0 <= y <= 20:
        return int(y)
    elif y < 0:
        return solution_y(x+1)
    elif y > 20:
        return solution_y(x-1)