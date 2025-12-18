"""
QUESTION:
Create a function named `is_prime(n)` that takes an integer as input and returns a boolean indicating whether the number is prime or not. The function should be implemented from scratch without using any built-in libraries or functions to determine primality. Use an optimized algorithm to efficiently check for primality, such as checking divisibility only up to the square root of the number. 

Then, create another function that takes an array 'a' containing at least 1000 elements as input, filters out only the prime numbers, and returns a new array 'b' containing these prime numbers in descending order.
"""

import math

def is_prime(n):
    """
    Checks if a number is prime.
    
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
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(5, sqrt_n, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def filter_primes(a):
    """
    Filters out only the prime numbers from the given array and returns them in descending order.
    
    Args:
    a (list): The input array containing at least 1000 elements.
    
    Returns:
    list: A new array containing only the prime numbers in descending order.
    """
    b = [num for num in a if is_prime(num)]
    b.sort(reverse=True)
    return b