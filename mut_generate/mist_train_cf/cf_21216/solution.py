"""
QUESTION:
Implement a function called `find_minimum_value` that takes an array of integers as input and returns the smallest integer value in the array without using built-in functions or methods for finding the minimum value. The function should have a time complexity of O(n) and minimal space complexity, where n is the number of elements in the array. The array may contain both positive and negative numbers, as well as duplicates.
"""

def find_minimum_value(arr):
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value