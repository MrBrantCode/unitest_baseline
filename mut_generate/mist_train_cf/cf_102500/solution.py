"""
QUESTION:
Create a function `isPrime(num)` that checks if a number is prime with a time complexity of O(sqrt(n)). The function should take an integer `num` as input and return a boolean indicating whether the number is prime or not. The function should be able to handle numbers between 1 and 100, inclusive, and should be optimized to only check divisibility up to the square root of the number. Note that the function will be used in a condition to filter prime numbers that are also divisible by 2.
"""

def is_prime(num: int) -> bool:
    """
    Checks if a number is prime with a time complexity of O(sqrt(n)).

    Args:
    num (int): The number to check for primality.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True