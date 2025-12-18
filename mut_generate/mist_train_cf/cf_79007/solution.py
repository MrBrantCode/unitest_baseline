"""
QUESTION:
Create a function `categorize_numbers` that takes a list of positive integers as input, categorizes the numbers into primes and composites, and returns two lists: one for prime numbers and one for composite numbers. The function should use a helper function `is_prime` to determine if a number is prime.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def categorize_numbers(lst):
    primes = []
    composites = []
    for number in lst:
        if is_prime(number):
            primes.append(number)
        else:
            composites.append(number)
    return primes, composites