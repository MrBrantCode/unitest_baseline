"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input and returns a new array with duplicate elements removed. The function should not use any built-in functions or libraries for removing duplicates and should have a time complexity of O(n) or less.
"""

def remove_duplicates(arr):
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements