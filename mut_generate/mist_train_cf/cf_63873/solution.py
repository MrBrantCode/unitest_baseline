"""
QUESTION:
Create a function named `get_first_five` that takes a numerical array as input and returns or prints the first five elements of the array. If the array has fewer than five elements, the function should return or print all the elements in the array.
"""

def get_first_five(num_array):
    first_five = num_array[:5]
    return first_five