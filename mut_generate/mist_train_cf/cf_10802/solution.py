"""
QUESTION:
Create a function named `find_primes` that takes two integers `start_range` and `end_range` as arguments and returns a list of all prime numbers between `start_range` and `end_range` (inclusive). The function should include a helper function named `is_prime` that checks if a number is prime.
"""

def is_prime(n):
    """Function to check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start_range, end_range):
    """Function to find all prime numbers between two numbers"""
    primes = []
    for num in range(start_range, end_range + 1):
        if is_prime(num):
            primes.append(num)
    return primes