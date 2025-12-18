"""
QUESTION:
Create a function `remove_duplicates(arr)` that takes an array of integers or floating-point numbers, removes all duplicates, and returns the array of unique elements in ascending order along with the count of unique elements. If the array is empty, return an empty array with a count of 0. The function should handle arrays with negative numbers and round floating-point numbers to the nearest integer before removing duplicates.
"""

def remove_duplicates(arr):
    if len(arr) == 0:
        return [], 0
    unique_elements = set(round(num) for num in arr)
    unique_array = list(unique_elements)
    unique_array.sort()
    return unique_array, len(unique_array)