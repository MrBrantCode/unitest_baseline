"""
QUESTION:
Write a function named `find_arr_sum` that takes two parameters: a list of integers `nums` and an integer `target`. The function should return all pairs of indices of elements in `nums` that sum up to `target`. The function should work with lists of varying lengths and `target` can be any integer between 0 and 100. The function should also work with lists containing both positive and negative numbers.
"""

def find_arr_sum(nums, target):
    if not nums or target is None:
        return []
    nums_dict = {}
    pairs = []
    for i, num in enumerate(nums):
        if (target - num) in nums_dict:
            pairs.append([nums_dict[target - num], i])
        nums_dict[num] = i
    return pairs