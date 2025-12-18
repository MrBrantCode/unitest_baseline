"""
QUESTION:
Create a function `cumulative_prime_sum` that takes an array of integers as input and returns the cumulative sum of prime numbers within the array. The function should utilize the `reduce` function and handle exceptions for non-numerical or negative values in the array. The function should return an error message if the input array contains non-integer values.
"""

from functools import reduce
import math

def cumulative_prime_sum(arr):
    """
    This function calculates the cumulative sum of prime numbers within the given array.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    int: The cumulative sum of prime numbers in the array.
    str: An error message if the input array contains non-integer values.
    """
    
    # Helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    try:
        # Filter out prime numbers
        primes = filter(is_prime, arr)
        
        # Calculate the cumulative sum
        total = reduce((lambda x, y: x + y), primes)
       
        return total
    except TypeError:
        return "Error: The array should only contain positive integers."
    except:
        return "Error: Unexpected error occurred."