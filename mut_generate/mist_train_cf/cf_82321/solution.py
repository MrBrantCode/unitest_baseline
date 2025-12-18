"""
QUESTION:
Write a function `product_array` that calculates the product of all numerical elements in a given array. The function should take an array of integers as input and return the product of all the numbers in the array. The array is not guaranteed to be non-empty, but it will only contain numerical elements.
"""

def product_array(nums):
    product = 1
    for num in nums:
        product *= num
    return product