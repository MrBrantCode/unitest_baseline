"""
QUESTION:
Write a function `find_max_value` that finds the maximum value in an unsorted array. The function should take an array as input, return the maximum value if the array is not empty, and return `None` if the array is empty.
"""

def find_max_value(array):
    if not array:
        return None
    
    max_value = array[0]

    for value in array:
        if value > max_value:
            max_value = value
            
    return max_value