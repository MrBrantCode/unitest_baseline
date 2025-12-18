"""
QUESTION:
Write a function named `product_except_self` that takes an array of numbers as input and returns an array where each element at index `i` is the product of all numbers in the input array except the number at index `i`. The function must not use division in its solution.
"""

def product_except_self(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    output = [1] * n
    
    for i in range(1, n):
        left_products[i] = left_products[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right_products[i] = right_products[i+1] * nums[i+1]
    
    for i in range(n):
        output[i] = left_products[i] * right_products[i]
    
    return output