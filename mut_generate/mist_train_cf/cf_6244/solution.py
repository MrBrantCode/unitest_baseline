"""
QUESTION:
Implement a function `find_unique_pairs` that takes a list of integers `nums` and a target integer `target` as input. The function should return a list of unique pairs of numbers from `nums` that add up to the target value. Each pair should be represented as a tuple with the smaller number first, and the pairs should be unique. The function should have a time complexity of O(n), where n is the length of the input list `nums`.
"""

def find_unique_pairs(nums, target):
    pair_set = set()
    result = set()
    
    for num in nums:
        complement = target - num
        
        if complement in pair_set:
            result.add(tuple(sorted((num, complement))))
        
        pair_set.add(num)
    
    return list(result)