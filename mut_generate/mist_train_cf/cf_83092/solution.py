"""
QUESTION:
Create a function named `product_except_self` that accepts an array of integers as input and returns an array of integers where each element is the product of all other elements in the input array except the element at the current index. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def entrance(nums):
    # Initialize an array to hold the result
    result = [1] * len(nums)

    # Calculate the product of all numbers to the left of each index
    left_product = 1
    for i in range(len(nums)):
        result[i] *= left_product
        left_product *= nums[i]

    # Calculate the product of all numbers to the right of each index
    right_product = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result