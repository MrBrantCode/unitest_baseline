"""
QUESTION:
Write a function called `find_max` that takes a list of integers and its start and end indices as input, and returns the maximum value in the list using a divide and conquer approach without using any built-in functions or methods for finding the maximum. The function should be able to handle lists of any length containing both positive and negative numbers.
"""

def find_max(arr, start, end):
    # Base case: only one element
    if start == end:
        return arr[start]

    # Divide the array into two halves
    mid = (start + end) // 2

    # Recursively find the maximum of each half
    max_left = find_max(arr, start, mid)
    max_right = find_max(arr, mid + 1, end)

    # Compare the maximum values from the two halves
    if max_left > max_right:
        return max_left
    else:
        return max_right