"""
QUESTION:
Find the function `twoSum` that takes two parameters: an array of integers `nums` and an integer `target`. The function should return the indices of the two numbers in `nums` that add up to `target`. 

The function must have a time complexity of O(n), where n is the length of `nums`. If multiple pairs of numbers add up to `target`, return the indices of the first pair encountered. A number cannot be used multiple times to form a pair that adds up to `target`, even if `nums` contains duplicate numbers. If no pair is found that adds up to `target`, return an empty array.
"""

def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []