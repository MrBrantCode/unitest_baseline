"""
QUESTION:
Implement a function named 'find_element' that takes an unordered array 'arr' and a target 'value' as input, and returns the index of the first occurrence of 'value' in 'arr' if found, or -1 if not found.
"""

def find_element(arr, value):
    for index, num in enumerate(arr):
        if num == value:
            return index
    return -1