"""
QUESTION:
Write a function called `filter_primes` that takes an array of integers as input and returns a new array containing only the prime numbers from the original array.
"""

def filter_primes(array):
    """Return a new array with only prime numbers from the original array"""
    def is_prime(n):
        """Check if number n is prime"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    return [n for n in array if is_prime(n)]