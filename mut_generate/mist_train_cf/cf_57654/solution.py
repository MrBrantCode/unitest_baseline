"""
QUESTION:
Write a function named `cumulative_mult` that takes an array of integers as input. The function should return an array where each element at index i is the product of all integers in the input array except for the integer at index i. The order of elements matters. The input array can be empty.
"""

def cumulative_mult(arr):
    n = len(arr)
    if n == 0:
        return []

    left_prod = [1]*n
    right_prod = [1]*n
    prod = [1]*n

    # compute left cumulative product for each element
    for i in range(1, n):
        left_prod[i] = arr[i-1] * left_prod[i-1]

    # compute right cumulative product for each element
    for i in range(n-2, -1, -1):
        right_prod[i] = arr[i+1] * right_prod[i+1]

    # product of left and right cumulative product is the
    # cumulative product of all elements except for the current element
    for i in range(n):
        prod[i] = left_prod[i] * right_prod[i]

    return prod