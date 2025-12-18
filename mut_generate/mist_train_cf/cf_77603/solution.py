"""
QUESTION:
Write a function named `sum_special_optimized` that calculates the sum of the products of all distinct pairs of elements in a given 1-dimensional array. The function should only use a single loop and leverage efficient algorithms or properties to minimize complexity. The function should not utilize existing library functions for operations like matrix multiplication or special numerical methods.
"""

def sum_special(arr):
    total_sum = sum(arr)
    cum_sum = 0
    result = 0
    for i in range(len(arr)):
        total_sum -= arr[i]
        result += arr[i] * total_sum
    return result