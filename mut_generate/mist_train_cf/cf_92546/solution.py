"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers and/or strings as input and returns a new array containing only the unique elements from the original array, in the order they first appear. The input array can contain duplicate elements, and the function should not modify the original array.
"""

def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements