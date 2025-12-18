"""
QUESTION:
Write a function `find_largest_prime_with_prime_digit_sum` that takes a vector of integers as input and returns the largest prime number in the vector that has the sum of its digits as a prime number. If no such prime number exists, return a message indicating that no prime was found with a digit sum as prime. The function should also include helper functions to check if a number is prime and to calculate the sum of the digits of a number. The input vector will contain only integers.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    """Calculate the sum of the digits of a number."""
    return sum(int(i) for i in str(n))

def find_largest_prime_with_prime_digit_sum(vector):
    """
    Find the largest prime number in a vector that has the sum of its digits as a prime number.
    
    Args:
        vector (list): A list of integers.
    
    Returns:
        int or str: The largest prime number with prime digit sum, or a message indicating no prime was found.
    """
    primes = [num for num in vector if is_prime(num) and is_prime(digit_sum(num))]
    
    if primes:
        return max(primes)
    else:
        return 'No prime found with digit sum as prime'