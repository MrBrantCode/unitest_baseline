"""
QUESTION:
Write a function `third_largest` that takes an array of integers as input and returns the third-largest unique element. If the array has less than three unique elements, the function should return an error message. The function should be able to handle negative numbers and zero.
"""

def third_largest(arr):
    unique_elements = list(set(arr))
    if len(unique_elements) < 3:
        return 'Error: there are less than 3 unique elements in the array!'
    else:
        unique_elements.sort(reverse=True)
        return unique_elements[2]