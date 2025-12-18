"""
QUESTION:
Write a function `find_maximum_subarray_sum` that finds the maximum subarray sum of an array, where the maximum subarray sum is the sum of the largest possible contiguous subarray within the array. The array can contain both positive and negative integers and may be empty. The time complexity of the solution should be O(n), where n is the length of the array.
"""

def find_maximum_subarray_sum(arr):
    if len(arr) == 0:
        return 0

    current_sum = max_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum