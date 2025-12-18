"""
QUESTION:
Create a function named `lowest_positive_integer` to find the lowest positive integer that cannot be represented as the sum of exactly three distinct prime numbers. The sum of the three primes must be the largest possible prime number less than or equal to the given positive integer.
"""

def lowest_positive_integer(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(num):
        """Get all prime numbers up to num."""
        primes = []
        for i in range(2, num + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def is_sum_of_three_primes(num, primes):
        """Check if a number is the sum of three distinct primes."""
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                for k in range(j + 1, len(primes)):
                    if primes[i] + primes[j] + primes[k] == num:
                        return True
        return False

    primes = get_primes(n)
    for i in range(n + 1, n * 2):
        if not is_sum_of_three_primes(i, primes):
            return i