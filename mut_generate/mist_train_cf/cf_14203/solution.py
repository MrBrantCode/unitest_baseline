"""
QUESTION:
Print all prime numbers within a given range in ascending order. The function should take two parameters: the lower and upper bounds of the range.
"""

def print_primes_in_range(lower, upper):
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [i for i in range(lower, upper + 1) if is_prime(i)]
    return sorted(primes)