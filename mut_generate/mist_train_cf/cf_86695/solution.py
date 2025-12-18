"""
QUESTION:
Write a function named `third_minimum` that takes a list of integers `nums` as input and returns the third minimum element in the list. The list is guaranteed to contain at least three elements and may contain negative numbers and duplicates.
"""

def third_minimum(nums):
    min1 = float('inf')
    min2 = float('inf')
    min3 = float('inf')
    
    for num in nums:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif min1 < num < min2:
            min3 = min2
            min2 = num
        elif min2 < num < min3:
            min3 = num
    
    return min3