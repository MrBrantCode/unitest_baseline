"""
QUESTION:
Create a function `sum_primes` that calculates the sum of all prime numbers within a specified interval. The function should take two parameters, `lower_limit` and `upper_limit`, representing the range of numbers to check for prime numbers. The function should return the sum of all prime numbers in the range `lower_limit` to `upper_limit` (inclusive). The solution should be efficient and handle large ranges.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True

def sum_primes(lower_limit, upper_limit):
    primes = [i for i in range(lower_limit, upper_limit+1) if is_prime(i)]
    return sum(primes)