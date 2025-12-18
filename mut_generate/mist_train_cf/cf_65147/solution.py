"""
QUESTION:
Write a function `max_product` that takes a list of integers as input and returns the maximum product of three distinct elements in the list. The function should consider both positive and negative numbers, as well as zeros. The input list is not guaranteed to be sorted and can contain duplicate elements. Implement the function in Python and analyze its time complexity.
"""

def max_product(nums):
    # Sort the list in ascending order
    nums.sort()
    # Calculate the product of the last three elements
    max1 = nums[-1] * nums[-2] * nums[-3]
    # Calculate the product of the first two elements and the last element
    max2 = nums[0] * nums[1] * nums[-1]
    # Return the maximum of the two products
    return max(max1, max2)