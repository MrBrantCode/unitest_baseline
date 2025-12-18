"""
QUESTION:
Write a function called `sum_of_primes` to find the sum of all prime numbers within a given range, from 1 to n (inclusive), where n is a positive integer. The function should take no arguments other than the range limit `n`.
"""

def sum_of_primes(n):
    """
    This function calculates the sum of all prime numbers within a given range from 1 to n (inclusive).
    
    Parameters:
    n (int): The upper limit of the range (inclusive).
    
    Returns:
    int: The sum of all prime numbers in the range.
    """
    
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    # Initialize the sum of primes
    sum_of_primes = 0
    
    # Iterate over the range from 1 to n (inclusive)
    for num in range(1, n + 1):
        # Check if the number is prime
        if is_prime(num):
            # If prime, add it to the sum
            sum_of_primes += num
    
    return sum_of_primes