"""
QUESTION:
Write a function named `update_array` that takes an array of integers as input and updates its elements in place to be their cube. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array, and n is a positive integer not exceeding 1000.
"""

def update_array(arr):
    n = len(arr)
    for i in range(n):
        arr[i] = arr[i] ** 3
    return arr