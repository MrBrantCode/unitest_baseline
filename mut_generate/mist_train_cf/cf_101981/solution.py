"""
QUESTION:
Write a function named `compute_odd_product` that takes an array of integers as input. The function should return the product of all odd elements in the array. If there are no odd elements, return 1.
"""

def compute_odd_product(arr):
    product = 1
    for num in arr:
        if num % 2 != 0:
            product *= num
    return product