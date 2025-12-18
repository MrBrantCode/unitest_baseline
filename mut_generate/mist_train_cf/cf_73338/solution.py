"""
QUESTION:
Write a function named `two_sum` that takes an array of integers `nums` and an integer `target` as input, and returns a list of two integers from the array whose sum equals the target value. The function should have a time complexity of O(n) and return the first pair found if there are multiple pairs that sum to the target.
"""

def two_sum(nums, target):
    hash_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement not in hash_dict:
            hash_dict[num] = i
        else:
            return [complement, num]
    return []