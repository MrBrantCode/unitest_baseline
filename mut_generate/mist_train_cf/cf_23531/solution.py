"""
QUESTION:
Write a function `max_product_pair` that calculates the maximum product of two numbers in a given list. The function should return the maximum product as an integer. The input list may contain both positive and negative integers.
"""

def max_product_pair(nums):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    
    for n in nums:
        if n > max1:
            max1, max2 = n, max1
        elif n > max2:
            max2 = n
        
        if n < min1:
            min1, min2 = n, min1
        elif n < min2:
            min2 = n
            
    return max(max1 * max2, min1 * min2)