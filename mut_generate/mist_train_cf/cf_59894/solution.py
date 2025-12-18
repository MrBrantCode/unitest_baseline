"""
QUESTION:
Implement a function named `product_of_primes` that takes a list of integers as input and returns the product of all prime numbers in the list, each raised to the power of its 1-indexed position in the list. Assume all input numbers are positive integers.
"""

def product_of_primes(num_list):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    prod = 1
    for i, num in enumerate(num_list, start=1):
        if is_prime(num):
            prod *= num ** i
    return prod