"""
QUESTION:
Create a function `sum_of_integers(x, y)` that takes two arguments and returns their sum. The function should only accept integer arguments, and it must be able to handle negative integers. If either of the arguments is not an integer, the function should return an error message.
"""

def entrance(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return "Error: Both arguments must be integers."
    else:
        return x + y