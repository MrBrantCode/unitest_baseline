"""
QUESTION:
Implement a function `sum_of_pairs(lst, target)` that takes a list of integers `lst` and a target integer `target` as input. The function should return the sum of all unique pairs of numbers in `lst` that add up to `target`. The function must have a time complexity of O(n), where n is the length of `lst`.
"""

def sum_of_pairs(lst, target):
    seen = set()
    result = 0
    
    for num in lst:
        complement = target - num
        if complement in seen:
            result += complement + num
        seen.add(num)
    
    return result