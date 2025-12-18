"""
QUESTION:
Write a function `sum_primes(arr)` that accepts an array of nested arrays containing integers and returns the sum of all prime numbers across all levels of arrays. The function should be able to handle an arbitrary amount of nesting within the arrays.
"""

def sum_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    total_sum = 0
    for item in arr:
        if isinstance(item, list):
            total_sum += sum_primes(item)
        elif is_prime(item):
            total_sum += item
    return total_sum