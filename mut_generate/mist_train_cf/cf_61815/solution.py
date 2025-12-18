"""
QUESTION:
Develop a function `sort_3d_list` that takes a 3-dimensional list as input and returns the list sorted by the values of the third element in each sub-sublist. The function should use Python's built-in sorting functionality and assume that each sub-sublist has at least three elements.
"""

def sort_3d_list(my_list):
    return sorted(my_list, key=lambda x: x[2])