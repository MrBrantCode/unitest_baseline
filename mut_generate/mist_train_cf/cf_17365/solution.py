"""
QUESTION:
Write a function `row_sum_primes(arr)` that takes a 2-dimensional array of positive integers as input. The function should return a list of the sums of each row, where the sum of each row is a prime number. If a row does not have a prime sum, it should be ignored and not included in the final result.
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