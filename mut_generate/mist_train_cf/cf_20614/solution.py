"""
QUESTION:
Write a function `sum_of_primes` that takes a list of integers as input and returns the sum of all the prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should handle lists of any length and contain any integers (positive, negative, or zero). The function should not use any built-in prime-checking functions or libraries.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(lst):
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum