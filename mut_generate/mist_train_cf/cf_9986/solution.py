"""
QUESTION:
Create a function `create_squared_dict` that takes a list of integers as input and returns a dictionary where the list items are the keys and the square of the items are the values. The function should not use any built-in Python functions or operators to calculate the square of a number, but instead should rely on basic arithmetic operations such as multiplication. The input list can contain any non-negative integers.
"""

def create_squared_dict(lst):
    squared_dict = {}
    for item in lst:
        squared_dict[item] = item * item
    return squared_dict