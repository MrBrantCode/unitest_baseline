"""
QUESTION:
Write a function `is_array_increasing_without_duplicates(arr)` that determines if the elements of the array are in strictly increasing order without any duplicates. The function should return True if the elements are in increasing order and False otherwise. The array may contain both positive and negative integers, and the function should have a time complexity of O(n), where n is the length of the array. Do not use any built-in sorting functions, methods, or additional data structures.
"""

def is_array_increasing_without_duplicates(arr):
    for i in range(len(arr) - 1):
        if arr[i] >= arr[i + 1]:
            return False
    return True