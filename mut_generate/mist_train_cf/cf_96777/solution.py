"""
QUESTION:
Write a function `find_average_of_primes` that takes a list of integers as input and returns the average of all prime numbers in the list that are greater than 100. Assume the input list is not empty and the average will not result in division by zero.
"""

def find_average_of_primes(numbers):
    """
    This function calculates the average of all prime numbers in the list that are greater than 100.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The average of prime numbers greater than 100.
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    prime_count = 0

    for num in numbers:
        if num > 100 and is_prime(num):
            prime_sum += num
            prime_count += 1

    return prime_sum / prime_count