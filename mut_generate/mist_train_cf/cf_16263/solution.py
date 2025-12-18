"""
QUESTION:
Write a function `sum_of_odd_primes` that calculates the sum of all odd prime numbers between two given positive integers, `lower_limit` and `upper_limit`, both of which are greater than 1. The function should take two parameters, `lower_limit` and `upper_limit`, and return the sum of odd prime numbers within the given range.
"""

def sum_of_odd_primes(lower_limit, upper_limit):
    """
    This function calculates the sum of all odd prime numbers between two given positive integers.

    Args:
        lower_limit (int): The lower limit of the range (inclusive).
        upper_limit (int): The upper limit of the range (inclusive).

    Returns:
        int: The sum of odd prime numbers within the given range.
    """

    # Initialize the sum
    sum_of_primes = 0

    # Iterate through the numbers between the lower and upper limits
    for num in range(lower_limit, upper_limit + 1):
        # Check if the number is odd
        if num % 2 != 0:
            # Check if the number is prime
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            # If the number is both odd and prime, add it to the sum
            if is_prime:
                sum_of_primes += num

    # Return the sum of odd prime numbers
    return sum_of_primes