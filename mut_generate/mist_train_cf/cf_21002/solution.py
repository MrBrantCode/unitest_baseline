"""
QUESTION:
Write a function named `max_difference` that takes an array of integers `nums` as input and returns the maximum difference between any two elements in the array. The function should have a time complexity of O(n) and use only a constant amount of extra space.
"""

def max_difference(nums):
    max_diff = 0
    min_num = float('inf')
    
    for num in nums:
        if num < min_num:
            min_num = num
        
        diff = num - min_num
        
        if diff > max_diff:
            max_diff = diff
    
    return max_diff