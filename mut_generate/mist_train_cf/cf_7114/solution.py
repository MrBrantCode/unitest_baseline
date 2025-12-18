"""
QUESTION:
Create a function f(x) that uses recursion to calculate the value of the polynomial x^3 + 4x^2 + 5x + 6 given the value of x. The function should handle negative values of x by returning "Invalid input".
"""

def entrance(x):
    if x < 0:
        return "Invalid input"
    else:
        return x * (x * (x + 4) + 5) + 6