"""
QUESTION:
Implement a function `check_sum_divisible_by_10(nums)` that takes an array of integers as input and returns `True` if the sum of any two integers in the array is divisible by 10, and `False` otherwise. The function should handle duplicate integers in the array and have a time complexity of O(n), where n is the number of elements in the array.
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