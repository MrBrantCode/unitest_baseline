"""
QUESTION:
Create a function 'add' that takes two optional integer parameters, x and y. The function should return the sum of x and y if both are integers. If one input is missing, return the other input if it's an integer. If neither or both inputs are missing, return an error message. If either or both inputs are not integers, return an error message.
"""

def add(x=None, y=None):
    if x is None and y is None:
        return "Error: You must provide at least one integer."
    elif x is None:
        if isinstance(y, int):
            return y
        else:
            return "Error: The provided input is not an integer."
    elif y is None:
        if isinstance(x, int):
            return x
        else:
            return "Error: The provided input is not an integer."
    else:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        else:
            return "Error: The provided inputs must be integers."