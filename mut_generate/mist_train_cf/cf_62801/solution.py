"""
QUESTION:
Write a function named `solve(arr, target)` that takes a two-dimensional array of integers and a target element as input. For each sub-array in the array, find the difference between the smallest and largest elements. Return a tuple containing the maximum of these differences and the total count of the target element in the array.
"""

def solve(arr, target):
    max_diff = float('-inf')
    target_count = 0
    for sub_arr in arr:
        max_sub_arr = max(sub_arr)
        min_sub_arr = min(sub_arr)
        diff = max_sub_arr - min_sub_arr
        if diff > max_diff:
            max_diff = diff
        target_count += sub_arr.count(target)
    return max_diff, target_count