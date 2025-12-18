"""
QUESTION:
Write a function `find_smallest` that takes a list of numbers as input and returns the smallest number in the list, handling cases where the list is empty.
"""

def find_smallest(array):
    if len(array) == 0:
        return None
    else:
        return min(array)