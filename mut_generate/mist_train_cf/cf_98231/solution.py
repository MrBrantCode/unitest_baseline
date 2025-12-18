"""
QUESTION:
Write a function named `extract_primes` that takes a list of integers as input and returns a list of prime numbers from the input list. The function should be efficient enough to handle large input lists without significant delay.
"""

def extract_primes(numbers):
    """
    Extract prime numbers from a list of integers.
    """
    def is_prime(n):
        """
        Check if a number is prime or not.
        """
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]