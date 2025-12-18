"""
QUESTION:
Write a function called `maximum_difference` that takes an array of integers as input and returns the maximum difference between two elements in the array such that the larger element appears after the smaller element in the array. If there are multiple pairs that satisfy this condition, return the maximum difference among all such pairs. Assume that the input array may contain less than two elements.
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