"""
QUESTION:
Write a recursive function called `sum_of_primes` that takes two parameters: `num` and `count`, and returns the sum of the first 15 prime numbers. The function should check for primality, increment the count when a prime number is found, and stop recursing when 15 prime numbers have been found. The input `num` should start at 2.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(num, count):
    if count == 15:
        return 0
    elif is_prime(num):
        return num + sum_of_primes(num + 1, count + 1)
    else:
        return sum_of_primes(num + 1, count)