"""
QUESTION:
Write a function called `average_of_primes` that calculates the average of all prime numbers greater than 100 in a given list of numbers. The function should take a list of integers as input and return the calculated average. If the list does not contain any prime numbers greater than 100, the function should return 0.
"""

def average_of_primes(numbers):
    """
    This function calculates the average of all prime numbers greater than 100 in a given list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        float: The calculated average of prime numbers greater than 100. If no such numbers exist, returns 0.
    """
    def is_prime(num):
        """Helper function to check if a number is prime."""
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

    return prime_sum / prime_count if prime_count != 0 else 0