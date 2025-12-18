"""
QUESTION:
Create a function named largest_prime_factor that takes an integer n as input and returns the largest prime factor of n that is greater than 100. The function should not take any other parameters.
"""

def largest_prime_factor(n):
    """
    This function finds the largest prime factor of a given number n that is greater than 100.

    Args:
        n (int): The number to find the largest prime factor of.

    Returns:
        int: The largest prime factor of n that is greater than 100.
    """

    # Define a helper function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize the largest prime factor
    largest_factor = 0

    # Iterate over all numbers from 100 to n
    for i in range(100, n + 1):
        # Check if the number is a factor of n
        if n % i == 0:
            # Check if the factor is a prime number
            if is_prime(i):
                # Update the largest prime factor
                largest_factor = i

    return largest_factor