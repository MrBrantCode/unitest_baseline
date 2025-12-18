"""
QUESTION:
Write a function called `find_second_largest` that takes a list of integers as input and returns the second largest number in the list. If the list has less than two unique elements, return -1.
"""

def entrance(nums):
    if len(nums) < 2:
        return -1
    
    largest = max(nums)
    second_largest = float('-inf')
    
    for num in nums:
        if num != largest and num > second_largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return -1
    
    return second_largest