"""
QUESTION:
Write a function `slope(a, b)` that calculates the slope of a line given its coefficients `a` and `b` as in the equation `ax + by + c = 0`. Use this function to find the value of `a` in the equation `ax + 2y + 3 = 0` if its slope is the negative reciprocal of the slope of the line `x + 2y + 3 = 0`.
"""

def calculate_slope(a, b):
    return -a/b

def find_value_of_a():
    # slope of first line
    m1 = calculate_slope(1, 2) 

    # slope of second line should be negative reciprocal of first line
    m2 = -1/m1 

    # coefficient of x in second line
    a = m2 * 2 

    return a

# or, simplified version of the above functions

def entrance(a, b):
    return (-1 / (-a/b)) * b 

# or, more simply

def entrance(a, b):
    return b / a 

# or, simplest form:

def entrance(a, b):
    return - (b / a)