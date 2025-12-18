"""
QUESTION:
Write a function `prodSigns(arr)` that calculates the sum of the absolute values of all elements in the array `arr`, multiplied by the product of the signs of the elements. The function should return `None` if the input array is empty. The sign of each element is considered as 1 for positive numbers, -1 for negative numbers, and 0 for zero.
"""

def prodSigns(arr):
    if not arr:
        return None
    
    abs_sum = sum(abs(num) for num in arr)
    sign_product = 1
    
    for num in arr:
        if num > 0:
            sign_product *= 1
        elif num < 0:
            sign_product *= -1
        else:
            sign_product *= 0
    
    return abs_sum * sign_product