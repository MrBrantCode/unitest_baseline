"""
QUESTION:
Implement a function named `linear_search` that takes an array and a target value as input and returns the index of the target value in the array. If the target value is not found, return -1. The function should have a time complexity of O(n), where n is the size of the array, as it needs to potentially iterate through every element in the array.
"""

def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # return the index of target
    return -1  # return -1 if target not found