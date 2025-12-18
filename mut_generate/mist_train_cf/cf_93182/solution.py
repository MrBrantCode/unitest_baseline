"""
QUESTION:
Given an array of integers, implement a function `check_sum_divisible_by_10` that checks if the sum of any two integers in the array is divisible by 10, handling potential duplicates in the array.
"""

def check_sum_divisible_by_10(nums):
    remainder_set = set()
    
    for num in nums:
        remainder = num % 10
        complement = (10 - remainder) % 10
        
        if complement in remainder_set:
            return True
        
        remainder_set.add(remainder)
    
    return False