"""
QUESTION:
Write a function `find_smallest_number` that takes a list of integers as input and returns the smallest positive integer not in the list. If the list is empty or contains no positive integers, the function should return 1. The function should handle lists containing negative numbers and zeros, but the output should be a positive integer.
"""

def find_smallest_number(nums):
    if not nums:
        return 1
    
    nums = [num for num in nums if num > 0]
    
    if not nums: 
        return 1
    
    max_num = max(nums)
    
    if 1 not in nums:
        return 1
    
    nums_set = set(range(1, max_num+1))
    
    return next((nums_set - set(nums)).__iter__(), max_num+1)