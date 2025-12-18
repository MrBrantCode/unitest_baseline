"""
QUESTION:
Create a function `productExceptSelf` that takes an array `nums` of integers as input and returns an array `output` where each element `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Implement the function with a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the input array.
"""

def productExceptSelf(nums):
    n = len(nums)
    output = [1] * n
    left_product = 1
    right_product = 1
    
    for i in range(n):
        output[i] *= left_product
        left_product *= nums[i]
        
        output[n - 1 - i] *= right_product
        right_product *= nums[n - 1 - i]
    
    return output