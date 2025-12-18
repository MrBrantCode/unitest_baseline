"""
QUESTION:
Write a function called `min_element` that takes an array of numbers as input and returns the smallest number in the array. Do not use any built-in functions or libraries to calculate the minimum value.
"""

def min_element(array):
    min_value = array[0]
    for item in array:
        if item < min_value:
            min_value = item
    return min_value