"""
QUESTION:
Write a function `find_max_subarray_sum(arr)` that takes a list of integers as input and returns the maximum sum of any contiguous subarray. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input list.
"""

def find_max_subarray_sum(arr):
    max_sum = 0
    current_sum = 0

    for num in arr:
        current_sum += num

        if current_sum < 0:
            current_sum = 0

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum