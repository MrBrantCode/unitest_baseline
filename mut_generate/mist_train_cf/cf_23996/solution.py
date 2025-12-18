"""
QUESTION:
Write a function called `find_max` that takes a list of integers as input and returns the maximum value in the list. The function should be able to handle a list of any length, but assume that the list is non-empty and contains only integers.
"""

def find_max(array):
    max = array[0]
    for element in array:
        if element > max:
            max = element
    return max