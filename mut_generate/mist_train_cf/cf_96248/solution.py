"""
QUESTION:
Write a function `find_pairs(nums, target)` that takes a list of integers `nums` and a target sum `target` as input, and returns a list of unique pairs of numbers in `nums` that add up to `target`. The list `nums` may contain negative numbers and duplicates, but the output should only include unique pairs. The order of the pairs in the output does not matter.
"""

def find_pairs(nums, target):
    pairs = set()
    seen = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((complement, num)))
            pairs.add(pair)
        seen.add(num)
    
    return list(pairs)