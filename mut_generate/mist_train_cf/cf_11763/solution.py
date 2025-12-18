"""
QUESTION:
Given an array of integers, write a function `maximum_difference(nums)` to find the maximum difference between two elements in the array such that the larger element appears after the smaller element. The function should return the maximum difference among all such pairs. The input array will contain at least two elements.
"""

def maximum_difference(nums):
    if len(nums) < 2:
        return 0
    
    min_element = nums[0]
    max_difference = 0
    
    for i in range(1, len(nums)):
        if nums[i] < min_element:
            min_element = nums[i]
        else:
            difference = nums[i] - min_element
            if difference > max_difference:
                max_difference = difference
    
    return max_difference