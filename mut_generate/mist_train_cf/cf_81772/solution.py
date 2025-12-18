"""
QUESTION:
Write a function named `prod_signs` that takes a list of integers as input and returns the sum of magnitudes of unique non-zero integers multiplied by the product of their signs. The signs are represented by 1 for positive numbers, -1 for negative numbers, and the function should ignore duplicates and zero values. If the input list is empty or contains only zero, the function should return None.
"""

def prod_signs(arr):
    if len(arr) == 0 or (len(arr) == 1 and arr[0] == 0):
        return None
    
    result = 0
    total_sign = 1
    seen = set()
    
    for num in arr:
        if num != 0:
            sign = 1 if num > 0 else -1
            total_sign *= sign
            seen.add(abs(num))
            
    result = total_sign * sum(seen)
    return result