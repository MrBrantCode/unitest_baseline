"""
QUESTION:
Create a function `is_prime` that determines if a given number is prime. The function should then be used to filter an array of 1000 random integers between -1000 and 1000, and print only the prime numbers in descending order.
"""

def is_prime(n):
    """
    Determines if a given number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True