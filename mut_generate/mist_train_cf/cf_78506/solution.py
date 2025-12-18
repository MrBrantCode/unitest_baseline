"""
QUESTION:
Create a function `func(x, y)` that takes two parameters and performs addition and subtraction operations on them. The function should only accept integer and float types for both parameters. If any parameter is not an integer or float, the function should return a custom error message indicating the incorrect type.
"""

def entrance(x, y):
    if not isinstance(x, (float, int)) or not isinstance(y, (float, int)):
        return "Error: Both inputs must be of integer or float type."
    else:
        z = x + y
        print(z)
        return x - y