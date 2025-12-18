"""
QUESTION:
Given an array of positive integers and a target value, create a function called `modify_array(arr, target)` that modifies the array such that each element is the multiplication of all the previous elements in the array and the target value. The resulting array should have the same length as the original array. 

The function must not use division and the target value can be any positive integer. The input array will always have at least one element and the resulting array should not contain any zeroes.
"""

def modify_array(arr, target):
    n = len(arr)
    result = [1] * n
    product = 1
    for i in range(n):
        result[i] *= product
        product *= arr[i]
    targetProduct = 1
    for i in range(n - 1, -1, -1):
        result[i] *= target * targetProduct
        targetProduct *= arr[i]
    return result