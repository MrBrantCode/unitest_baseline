"""
QUESTION:
Write a function named `product_except_self` that takes a list of numbers as input and returns a new list where each element at index i is the product of all other elements in the list except the element at index i. The input list does not contain any zeros. The solution should have a time complexity of O(n), where n is the length of the input list.
"""

def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    
    # Calculate the product of all elements to the left of each element
    left_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    
    # Calculate the product of all elements to the right of each element
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    
    return result