"""
QUESTION:
Create a function `print_and_count_primes` that takes a list of integers as input. The function should print all the prime numbers in the list and also return the total count of prime numbers. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input list can contain duplicate values and non-prime numbers. The function should not take any other parameters besides the input list.
"""

def print_and_count_primes(numbers):
    """
    This function prints all prime numbers in the given list and returns the total count of prime numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The total count of prime numbers in the list.
    """

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    prime_count = 0
    for num in numbers:
        if is_prime(num):
            print(num)
            prime_count += 1
    return prime_count