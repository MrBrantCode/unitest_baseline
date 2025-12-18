"""
QUESTION:
Write a function `row_sum_divisible_by_n(arr, n)` that takes a 2D array `arr` and an integer `n` as input. The function should calculate the sum of elements in each row of the array, check if the sum is divisible by `n`, and return a list of row indices where the sum is divisible by `n`. If no rows meet this condition, the function should return an empty list.
"""

def row_sum_divisible_by_n(arr, n):
    return [i for i, row in enumerate(arr) if sum(row) % n == 0]