"""
QUESTION:
Write a function called `is_increasing_strict` that takes an array of integers as input and returns True if the array elements are in strictly increasing order without any duplicate elements. The function should have a time complexity of O(n) and should not use any built-in sorting functions or methods, or additional data structures.
"""

def is_increasing_strict(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return False
    return True