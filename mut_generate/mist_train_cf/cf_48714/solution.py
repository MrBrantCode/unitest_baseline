"""
QUESTION:
Create a function named `cumulative_product` that calculates the cumulative product of the constituents within a given integer array. The input array can contain multiple integers, and the output should be the product of all integers in the array. The function should return an integer result.
"""

def cumulative_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product