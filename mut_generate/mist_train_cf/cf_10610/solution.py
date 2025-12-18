"""
QUESTION:
Write a function `row_sums(arr)` that takes a 2-dimensional array `arr` of positive integers as input. The function should calculate the sum of each row in the array, and if the sum of a row is a prime number, include it in the output. Return a list of the sums of each row that satisfy the prime number constraint.
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