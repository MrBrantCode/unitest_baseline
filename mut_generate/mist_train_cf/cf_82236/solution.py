"""
QUESTION:
Write a function named `max_in_array` that takes an array of at least 3 distinct positive integers and returns the maximum element in the array using the `reduce` method. Ensure the array consists of at least 3 distinct elements and only contains positive integers.
"""

from functools import reduce

def max_in_array(array):
    return reduce(lambda a, b: a if a > b else b, array)