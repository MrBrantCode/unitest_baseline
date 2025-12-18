"""
QUESTION:
Write a function `find_first_occurrence` that takes in a list of at least 5 unique integers and an element, and returns the index of the first occurrence of the element in the list. If the element is not present, return -1. Implement the function with a time complexity of O(n) and a space complexity of O(1) using only basic array operations.
"""

def find_first_occurrence(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1