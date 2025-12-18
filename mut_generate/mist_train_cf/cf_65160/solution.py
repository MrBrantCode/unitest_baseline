"""
QUESTION:
Create a function `prod_signs` that takes a non-zero integer array `arr` with no duplicates and no more than 100 elements. The function should calculate the sum of the absolute values of the array elements multiplied by their respective signs. If the array is empty or contains any zero, return `None`.
"""

def prod_signs(arr):
    if not arr:  
        return None
    
    val, sign = 0,1

    for num in arr:
        if num == 0:  
            return None
        else:   
            val += abs(num)*(1 if num>0 else -1)
    return val 