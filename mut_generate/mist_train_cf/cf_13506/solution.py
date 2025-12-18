"""
QUESTION:
Create a function `modify_array(arr, target)` that takes an array of positive integers `arr` and a target value `target` as input. Modify the array such that each element at index `i` is the product of the target value and all elements in the array up to but not including `i`. The resulting array should have the same length as the original array.
"""

def modify_array(arr, target):
    result = [0] * len(arr)
    product = target
    
    for i in range(len(arr)):
        result[i] = product
        product *= arr[i]
    
    return result