"""
QUESTION:
Implement a function `find_minimum_value(arr)` that finds the minimum value from a given array without using built-in functions or methods for finding the minimum value. The function should have a time complexity of O(n), where n is the number of elements in the array, and minimize space complexity. The array may contain both positive and negative numbers, and may contain duplicates. In case of duplicates, the function should return the smallest value among them.
"""

def find_minimum_value(arr):
    min_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
    return min_value