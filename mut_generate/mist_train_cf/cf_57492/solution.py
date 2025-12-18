"""
QUESTION:
Create a function called `sum_array()` that takes an array of integers as input and returns the sum of its elements without using a loop. The function should be able to handle an empty array, in which case it should return 0.
"""

def sum_array(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])