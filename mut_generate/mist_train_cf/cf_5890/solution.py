"""
QUESTION:
Write a function named `find_primes` that takes a list of integers as input and returns a list of prime numbers from the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input list can contain negative numbers.
"""

def find_primes(lst):
    return [num for num in lst if num > 1 and all(num % i != 0 for i in range(2, int(abs(num)**0.5)+1))]