"""
QUESTION:
Write a function `sum_of_square_numbers(N)` that takes a positive integer `N` greater than 10 as input, calculates the sum of squares of the first `N` natural numbers using only bitwise operations and without using any arithmetic operators, and returns the sum. The function should have a time complexity of O(N) and a space complexity of O(1).
"""

def sum_of_square_numbers(N):
    sum = ((N * (N + 1) * ((N << 1) + 1)) >> 1) // 3
    return sum