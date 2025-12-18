"""
QUESTION:
Write a function named `find_first_occurrence` that takes in a list of at least 5 unique integers and an element, and returns the index of the first occurrence of the element in the list. If the element is not present in the list, return -1. Implement this function with a time complexity of O(n) and a space complexity of O(1), and do not use any built-in functions or libraries.
"""

def find_first_occurrence(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1