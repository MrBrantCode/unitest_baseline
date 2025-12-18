"""
QUESTION:
Create a function named `find_max` that takes a list of integers as input, where the list can contain negative numbers and null values. The function should return the maximum element in the list without using any built-in functions or methods. If the list only contains null values or is empty, the function should return null.
"""

def find_max(my_list):
    max_val = None
    for val in my_list:
        if val is not None:
            if max_val is None or val > max_val:
                max_val = val
    return max_val