"""
QUESTION:
Write a function `find_max_primes(numbers)` that takes a list of positive integers as input and returns a tuple containing the maximum prime number and the second maximum prime number. If there are less than two prime numbers in the list, return the maximum prime number and 0.
"""

import math

def find_max_primes(numbers):
    """
    This function finds the maximum prime number and the second maximum prime number in a list of positive integers.
    
    Args:
    numbers (list): A list of positive integers.
    
    Returns:
    tuple: A tuple containing the maximum prime number and the second maximum prime number.
    If there are less than two prime numbers in the list, return the maximum prime number and 0.
    """

    # Initialize variables
    maxPrime = 0
    secondMaxPrime = 0

    # Iterate through each number in the array
    for num in numbers:
        # Check if the number is prime
        isPrime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                isPrime = False
                break
        
        # Update maxPrime and secondMaxPrime
        if isPrime:
            if num > maxPrime:
                secondMaxPrime = maxPrime
                maxPrime = num
            elif num > secondMaxPrime and num != maxPrime:
                secondMaxPrime = num

    return (maxPrime, secondMaxPrime)