"""
QUESTION:
Write a function `row_sum_primes` that takes a 2-dimensional array of positive integers as input. The function should return a list of sums of rows where the sum is a prime number, ignoring rows with non-prime sums.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def row_sum_primes(arr):
    result = []
    for row in arr:
        row_sum = sum(row)
        if is_prime(row_sum):
            result.append(row_sum)
    return result