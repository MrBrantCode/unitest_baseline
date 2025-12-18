"""
QUESTION:
Write a function named `sum_of_primes` that takes a list of integers as input. Calculate the sum of all the prime numbers in the list, ignoring any even numbers that are adjacent to a prime number. Assume the input list may contain both positive and negative integers.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(numbers):
    """
    Calculate the sum of all the prime numbers in the list, 
    ignoring any even numbers that are adjacent to a prime number.
    
    Parameters:
    numbers (list): A list of integers.
    
    Returns:
    int: The sum of all prime numbers in the list.
    """
    total = 0
    for i in range(len(numbers)):
        if is_prime(abs(numbers[i])):
            if i == 0 or numbers[i-1] % 2 != 0:
                if i == len(numbers) - 1 or numbers[i+1] % 2 != 0:
                    total += numbers[i]
    return total