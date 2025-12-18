"""
QUESTION:
Write a function `find_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list, with no duplicates. The function should use list comprehension.
"""

def find_prime_numbers(input_list):
    primes = [x for x in input_list if all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1]
    primes = list(set(primes))
    return primes