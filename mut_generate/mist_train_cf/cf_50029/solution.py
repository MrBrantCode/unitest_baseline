"""
QUESTION:
Create a function named `sum_prime_numbers` that takes an array of integers as input and returns the sum of all prime numbers in the array.
"""

def sum_prime_numbers(nums):
    """Compute the summation of all primes in the list nums."""
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return sum(num for num in nums if is_prime(num))