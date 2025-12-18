"""
QUESTION:
Create a function `find_pairs(nums, target)` that takes a list of integers `nums` and a target sum `target`. Return a list of all pairs of integers from `nums` that add up to `target`, or an empty list if no such pairs exist. The function should have a time complexity of O(n), where n is the length of `nums`.
"""

def find_pairs(nums, target):
    pairs = []
    num_dict = {}
    
    for num in nums:
        complement = target - num
        if complement in num_dict:
            pairs.append([complement, num])
        num_dict[num] = True
    
    return pairs