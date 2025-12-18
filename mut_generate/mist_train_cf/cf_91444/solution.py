"""
QUESTION:
Write a function `row_sums(arr)` that takes a 2-dimensional array `arr` of positive integers as input and returns a list of the sums of each row, where the sum of each row must be a prime number. If a row's sum is not a prime number, exclude it from the result.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def row_sums(arr):
    result = []
    for row in arr:
        row_sum = sum(row)
        if is_prime(row_sum):
            result.append(row_sum)
    return result