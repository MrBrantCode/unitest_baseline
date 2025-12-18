"""
QUESTION:
Write a function `sum_of_primes` that takes a list of integers as input and returns the sum of all the prime numbers in the list. The function should only consider numbers greater than 1 as potential prime numbers and should be able to handle lists of arbitrary length.
"""

def is_prime(num):
    # Check if a number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(lst):
    # Find the sum of all prime numbers in the list
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum