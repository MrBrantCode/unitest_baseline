"""
QUESTION:
Write a function `smallest_subarray_with_sum` that takes an array of integers and a target sum as input. The function should return the length of the smallest subarray in the input array that has a sum greater than or equal to the target sum. If no such subarray exists, the function should return -1. The function must have a time complexity of O(n), where n is the length of the input array, and use constant space.
"""

def smallest_subarray_with_sum(arr, target):
    n = len(arr)
    min_len = float('inf')
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum >= target:
            min_len = min(min_len, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    if min_len == float('inf'):
        return -1
    else:
        return min_len