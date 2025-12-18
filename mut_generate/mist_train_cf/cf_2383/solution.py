"""
QUESTION:
Write a function `max_pairwise_product(arr)` that takes an array of integers `arr` as input and returns the maximum pairwise product of those numbers. The function should have a time complexity of O(n^2), where n is the length of the array, and should not use any built-in sorting algorithms.
"""

def max_pairwise_product(arr):
    n = len(arr)
    max_product = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return max_product