"""
QUESTION:
Write a function `sum_of_primes` that calculates the sum of the first n prime numbers in a given array, where n is a multiple of 3. The array only contains prime numbers and is not empty. The function should return the sum as an integer.
"""

def sum_of_primes(arr, n):
    """
    Calculate the sum of the first n prime numbers in a given array.

    Args:
        arr (list): A list of prime numbers.
        n (int): The number of prime numbers to sum.

    Returns:
        int: The sum of the first n prime numbers.
    """
    return sum(arr[:n])