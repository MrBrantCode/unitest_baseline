"""
QUESTION:
Create a function `find_index(arr, target)` that takes an array of integers and an integer as input, and returns the index of the first occurrence of the integer in the array. The function should have a time complexity of O(n^2) and handle arrays with duplicate values and negative integers. If the given integer is not found in the array, return -1.
"""

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1