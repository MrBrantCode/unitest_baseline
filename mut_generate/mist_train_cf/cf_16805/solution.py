"""
QUESTION:
Write a function called `find_max` that finds the maximum value in an array of integers using a divide and conquer approach. The function should take three parameters: the array and two indices representing the range of the array to consider (start and end). It should not use any built-in functions or methods for finding the maximum, and it should handle arrays containing both positive and negative numbers. The function should return the maximum value in the specified range of the array.
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
    return max(max_left, max_right)