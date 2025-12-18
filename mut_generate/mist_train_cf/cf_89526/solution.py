"""
QUESTION:
Write a function `find_minimum_value` that finds the minimum value in a given array without using built-in functions or methods for finding the minimum value. The function should have a time complexity of O(n) and minimize space complexity. The function must not use any additional data structures, modify the original array, or handle an array of size greater than 10^6. If the array is empty, the function should return an error message.
"""

def find_minimum_value(arr):
    if len(arr) == 0:
        return "Error: The array is empty."

    min_value = float('inf')  # Initialize with maximum possible value

    for num in arr:
        if num < min_value:
            min_value = num

    return min_value