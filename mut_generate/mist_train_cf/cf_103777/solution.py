"""
QUESTION:
Write a function called `calculate_product` that takes an array of integers as input and returns the product of all elements in the array. The function should handle arrays containing both positive and negative integers.
"""

def calculate_product(arr):
    product = 1
    for num in arr:
        product *= num
    return product