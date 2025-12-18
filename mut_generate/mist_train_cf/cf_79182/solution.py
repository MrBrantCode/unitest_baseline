"""
QUESTION:
Write a function named `max_sum_subarray` that takes an array of integers as input and returns the maximum cumulative sum achievable by summing up the consecutive elements within the array. The function should be efficient and run in linear time complexity, i.e., O(n), where n is the number of elements in the array.
"""

def max_sum_subarray(arr):
    global_max = current_max = arr[0]
    for num in arr[1:]:
        current_max = max(num, current_max + num)
        global_max = max(global_max, current_max)
    return global_max