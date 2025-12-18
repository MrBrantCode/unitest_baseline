"""
QUESTION:
Write a function named `sum_of_products` that calculates the sum of the products of all possible subarrays within a given list. The list can contain integers and/or floating point numbers, and may include negative numbers and zeros. The function should be efficient and able to handle large lists without significant performance degradation. The input list can also contain duplicate numbers.
"""

def sum_of_products(lst):
    n = len(lst)
    product_sum = 0
    for i in range(n):
        product_sum += lst[i] * (n - i) * (i + 1)
    return product_sum