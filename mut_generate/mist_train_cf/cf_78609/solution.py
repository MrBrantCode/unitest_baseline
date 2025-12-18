"""
QUESTION:
Write a function named `sum_primes` that calculates the sum of the first 10 positive prime numbers within a given range defined by `range_start` and `range_end`. The function should return the sum of the first 10 prime numbers found in the range.
"""

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False    
    return True


def sum_primes(range_start, range_end):
    primes = []

    for i in range(range_start, range_end):
        if len(primes) == 10:
            break
        elif is_prime(i):
            primes.append(i)
    return sum(primes)