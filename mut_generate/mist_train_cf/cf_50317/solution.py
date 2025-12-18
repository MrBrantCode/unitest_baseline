"""
QUESTION:
Write a function named `max_subarray_sum` that finds the maximum sum of a contiguous subarray within a given array. The function should also return the start and end indices of the subarray that generates this maximum sum. The solution must have a time complexity less than O(n^2) and be able to handle arrays containing negative numbers.
"""

def max_subarray_sum(arr):
    max_sum = float('-inf')
    curr_sum = 0
    start = end = 0
    temp_start = 0

    for i in range(len(arr)):
        if curr_sum <= 0:
            curr_sum = arr[i]
            temp_start = i
        else:
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            start = temp_start
            end = i

    return max_sum, (start, end)