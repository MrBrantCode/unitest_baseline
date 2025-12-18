"""
QUESTION:
Write a function called `modify_array` that takes an array of positive integers and a target value as input, and returns a new array where each element is the product of all previous elements in the array and the target value. The resulting array should have the same length as the original array. Note that you cannot use division in your solution, the target value can be any positive integer, the input array will always have at least one element, and the resulting array should not contain any zeroes.
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
        result[i] *= targetProduct * target
        targetProduct *= arr[i]
    return result