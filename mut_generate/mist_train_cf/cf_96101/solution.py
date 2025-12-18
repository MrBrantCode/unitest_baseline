"""
QUESTION:
Write a function named `find_sum` that takes an array of integers as input and returns the maximum sum of a contiguous subarray within the given array. The function must have a time complexity of O(n), where n is the number of elements in the array, and it must use a constant amount of space. The function should handle arrays containing negative numbers and return the correct maximum sum.
"""

def find_sum(arr):
    if len(arr) == 0:
        return 0

    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum