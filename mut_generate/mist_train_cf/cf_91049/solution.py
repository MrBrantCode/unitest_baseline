"""
QUESTION:
Write a function `find_max` that takes an array of integers as input and returns the maximum number without using any inbuilt functions, loops, or recursion. Assume the array has at least one element.
"""

def find_max(array):
    max_num = array[0]
    for element in array[1:]:
        if element > max_num:
            max_num = element
    return max_num