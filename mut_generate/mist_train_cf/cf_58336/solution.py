"""
QUESTION:
Write a function `max_pair_sum` that takes an array of integers as input and returns the maximum sum of any two distinct elements in the array. The function should not use any built-in sorting functions.
"""

def max_pair_sum(arr):
    max1 = -float('inf')
    max2 = -float('inf')
    
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return max1 + max2