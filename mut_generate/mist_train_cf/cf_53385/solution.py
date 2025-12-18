"""
QUESTION:
Create a function named `list_operation` that takes two single-element lists `x` and `y` as input, where each element is a number. The function should return the result of the following operations: add the elements of `x` and `y`, then subtract the elements of `x` from the result. The function should use list comprehension and the `zip` function.
"""

def list_operation(x, y):
    return [(xi+yi)-xi for xi, yi in zip(x, y)][0]