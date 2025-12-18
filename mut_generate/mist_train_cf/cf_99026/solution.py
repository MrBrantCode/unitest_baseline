"""
QUESTION:
Create a function named `multiply` that takes two parameters, `a` and `b`. The function should return the product of `a` and `b` if both are integers or floats. However, if either `a` or `b` is not an integer or float, the function should print an error message and return `None`.
"""

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Error: Inputs must be integers or floats.")
        return None
    return a * b