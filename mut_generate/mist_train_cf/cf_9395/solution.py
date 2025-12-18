"""
QUESTION:
Design a function named 'find_largest_number' that takes an array of integers as input and returns the largest number in the array. The function should not use any built-in sorting functions and should have a time complexity of O(n), where n is the number of elements in the array.
"""

def find_largest_number(arr):
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num