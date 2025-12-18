"""
QUESTION:
Write a function to generate a new list containing the cubes of prime numbers from a given list. The function should take a list of integers as input and return a new list with the cubes of the prime numbers. Assume that the input list only contains positive integers.
"""

def prime_cubes(numbers):
    """
    Generate a new list containing the cubes of prime numbers from a given list.

    Args:
    numbers (list): A list of integers.

    Returns:
    list: A new list with the cubes of the prime numbers.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [x**3 for x in numbers if is_prime(x)]