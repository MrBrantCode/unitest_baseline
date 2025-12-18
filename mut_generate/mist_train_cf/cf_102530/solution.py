"""
QUESTION:
Create a function named `sort_array` that takes an array of integers as input and returns a string representation of the array sorted in ascending order. The output string should have the numbers separated by commas and enclosed in square brackets. The input array will have at least 10 integers and may contain negative numbers.
"""

def sort_array(arr):
    arr.sort()  # Sort the array in ascending order
    return '[' + ','.join(map(str, arr)) + ']'  # Convert the array to a string