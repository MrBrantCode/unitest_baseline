"""
QUESTION:
Create a function named `square` that takes one argument `x`. The function should return the square of `x` if `x` is a positive number. If `x` is not a positive number, return "Invalid input". Use a lambda expression with a conditional statement to implement this function.
"""

def square(x):
    return x * x if x > 0 else "Invalid input"