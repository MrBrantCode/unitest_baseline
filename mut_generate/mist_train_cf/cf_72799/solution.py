"""
QUESTION:
Write a function `square_numbers(lst)` that takes a list of elements as input, squares the numeric elements (both integers and floats), and returns them in a new list while ignoring non-numeric elements. The function should not crash when encountering non-numeric elements.
"""

def square_numbers(lst):
    return [item ** 2 for item in lst if isinstance(item, (int, float))]