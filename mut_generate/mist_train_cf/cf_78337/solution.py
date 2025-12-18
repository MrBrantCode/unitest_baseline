"""
QUESTION:
Write a function named `calculate_product` that takes a list of integers as input and returns the product of all the elements in the list. The function should handle lists of any length.
"""

def calculate_product(nums):
    product = 1
    for num in nums:
        product *= num
    return product