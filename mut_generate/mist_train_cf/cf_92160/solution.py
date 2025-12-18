"""
QUESTION:
Write a function `compute_product(arr)` that takes an array of integers as input and returns the product of all elements that are multiples of 3, excluding any elements equal to 4. The function should handle both positive and negative numbers.
"""

def compute_product(arr):
    product = 1
    for num in arr:
        if num % 3 == 0 and num != 4:
            product *= num
    return product