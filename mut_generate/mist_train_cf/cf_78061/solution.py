"""
QUESTION:
Write a function named "compute" that takes a list of integers as input and returns the product of all digits in the smallest prime number found in the list. If no prime numbers are found, the function should return 0.
"""

def compute(lst):
    def is_prime(n):
        """Helper function to check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0

    smallest_prime = min(primes)
    product = 1
    while smallest_prime:
        product *= smallest_prime % 10
        smallest_prime //= 10

    return product