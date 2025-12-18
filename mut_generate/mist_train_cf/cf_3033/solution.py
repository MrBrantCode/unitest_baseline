"""
QUESTION:
Write a function `max_product(arr, m)` that computes the maximum product of `m` consecutive values in the given array `arr`. If the array contains less than `m` elements, consider the maximum product as the smallest possible value. If there are multiple subsequences with the same maximum product, return the one with the latest starting index. The array may contain negative numbers, non-integer values, or duplicate values.
"""

def max_product(arr, m):
    if len(arr) < m:
        return float('-inf')
    
    max_product = float('-inf')
    start_index = 0
    current_product = 1
    
    for i in range(m):
        current_product *= arr[i]
        
    if current_product > max_product:
        max_product = current_product
        start_index = 0
        
    for i in range(m, len(arr)):
        current_product /= arr[i - m]
        current_product *= arr[i]
        
        if current_product > max_product:
            max_product = current_product
            start_index = i - m + 1
            
    return max_product