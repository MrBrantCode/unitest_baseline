"""
QUESTION:
Write a function `find_sum(arr)` that calculates the sum of the maximum subarray within a given array. The function should have a time complexity of O(n), where n is the number of elements in the array, and use a constant amount of space. The array may contain negative numbers.
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