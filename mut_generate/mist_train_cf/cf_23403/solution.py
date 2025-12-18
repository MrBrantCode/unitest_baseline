"""
QUESTION:
Write a function called `find_max_element` that takes an array of integers as input and returns the maximum element in the array. The function should be able to handle arrays of any length.
"""

def find_max_element(array):
    max_element = array[0]
    for element in array:
        if element > max_element:
            max_element = element
    return max_element