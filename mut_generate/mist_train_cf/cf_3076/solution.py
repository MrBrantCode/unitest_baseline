"""
QUESTION:
Implement a function `max_product_with_negative(arr)` that finds the maximum product of three numbers in an array, where at least one of the numbers must be negative. Return 0 if no such triplet exists. The function must have a time complexity of O(n) or better and a space complexity of O(1) or better, and must not modify the original array.
"""

def max_product_with_negative(arr):
    if len(arr) < 3:
        return 0
    
    max1 = max2 = max3 = float('-inf')
    min1 = min2 = float('inf')
    
    for num in arr:
        if num > max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num > max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num
            
        if num < min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num
    
    return max(max1 * max2 * max3, min1 * min2 * max1, 0)