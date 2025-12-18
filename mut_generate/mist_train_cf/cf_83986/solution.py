"""
QUESTION:
Write a function `product_except_self(nums)` that takes an array of numbers as input and returns an array where each element at index `i` is the product of all numbers in the input array except the number at index `i`. The function should not use division and should work even if the input array contains zeros. The time complexity of the function should be O(n).
"""

def product_except_self(nums):
    length = len(nums)
    output = [1]*length
    left = right = 1
    
    for i in range(length):
        output[i] *= left
        output[length-1-i] *= right
        left *= nums[i]
        right *= nums[length-1-i]
    
    return output