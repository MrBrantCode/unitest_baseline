"""
QUESTION:
Write a function `find_minimum_value` that takes an array of integers as input and returns the minimum value from the array. The function must not use any built-in functions or methods for finding the minimum value. It should have a time complexity of O(n) and minimize the space complexity. The function should handle an array with both positive and negative numbers, duplicates, and edge cases such as an empty array, an array with all elements being the same value, and an array with all elements being 0.
"""

def find_minimum_value(arr):
    if len(arr) == 0:
        return "Error: The array is empty."

    min_value = float('inf')  # Initialize with maximum possible value

    for num in arr:
        if num < min_value:
            min_value = num

    return min_value