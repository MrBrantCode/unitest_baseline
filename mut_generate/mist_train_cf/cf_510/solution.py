"""
QUESTION:
Create a function `find_max_num` that takes a list of integers as input, ignores any negative numbers and numbers divisible by 3, and returns the maximum number in the list. The function should have a time complexity of O(n) and should not use any built-in functions or libraries for finding the maximum number.
"""

def find_max_num(nums):
    max_num = None
    
    for num in nums:
        if num < 0 or num % 3 == 0:
            continue
        
        if max_num is None:
            max_num = num
        elif num > max_num:
            max_num = num
            
    return max_num