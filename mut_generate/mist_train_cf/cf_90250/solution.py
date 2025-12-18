"""
QUESTION:
Create a function named `find_index` that takes an array of integers and an integer as input, and returns the index of the first occurrence of the integer in the array. The function should have a time complexity of O(n), where n is the length of the array, and should return -1 if the given integer is not found in the array.
"""

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1