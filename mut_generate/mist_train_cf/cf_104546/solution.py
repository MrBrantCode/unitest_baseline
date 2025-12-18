"""
QUESTION:
Write a function `check_unique_elements` that takes a list of integers as input and returns the count of unique elements in the list. Also, the function should check if all elements in the list are equal and return a corresponding message.
"""

def check_unique_elements(arr):
    unique_elements = set(arr)
    if len(unique_elements) == 1:
        return f"All elements are equal, count of unique elements: {len(unique_elements)}"
    else:
        return f"Not all elements are equal, count of unique elements: {len(unique_elements)}"