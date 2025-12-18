"""
QUESTION:
Create a function to calculate the sum of all prime numbers within a specified range. The function should take two parameters: `start` and `end`, representing the start and end of the range (inclusive). The function should return the sum of all prime numbers within the range. The range will always be within the integer limits, and `start` will always be less than or equal to `end`.
"""

def sum_of_primes_in_range(start, end):
    """
    Calculate the sum of all prime numbers within a specified range.

    Args:
        start (int): The start of the range (inclusive).
        end (int): The end of the range (inclusive).

    Returns:
        int: The sum of all prime numbers within the range.
    """

    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Initialize sum of primes
    sum_of_primes = 0

    # Loop through the range to find the sum of prime numbers
    for num in range(start, end + 1):
        if is_prime(num):
            sum_of_primes += num

    return sum_of_primes