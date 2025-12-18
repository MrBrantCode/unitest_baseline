"""
QUESTION:
Write a function named `count_up_to(n)` that takes a non-negative integer `n` as input and returns a list of prime numbers smaller than `n`. The function should return an empty list for inputs 0 and 1, and include prime numbers starting from 2 for inputs greater than 1.
"""

def count_up_to(n):
    """Implement a function that takes a non-negative integer and returns a list of prime numbers below n."""
    def is_prime(number):
        """Check if a given number is prime."""
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes