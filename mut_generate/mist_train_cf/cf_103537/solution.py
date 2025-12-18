"""
QUESTION:
Create a function named `remove_duplicates` that takes an array of integers and/or strings as input, removes duplicates while preserving the original order of elements, and returns the resulting array. The function should not use any built-in functions that remove duplicates or sort the array.
"""

def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements