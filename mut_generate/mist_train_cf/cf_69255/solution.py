"""
QUESTION:
Write a function `compute_sum(numbers)` that takes a list of integers `numbers` as input and returns the sum of the second smallest and second largest primary (non-composite) numbers in the list. If the list does not contain at least two primary numbers, the function should return `None`. The list can contain both positive and negative integers, but primary numbers are only defined for positive integers.
"""

def compute_sum(numbers):
    """
    This function calculates the sum of the second smallest and second largest primary (non-composite) numbers in a list.
    
    Parameters:
    numbers (list): A list of integers containing both positive and negative numbers.
    
    Returns:
    int or None: The sum of the second smallest and second largest prime numbers, or None if the list contains fewer than two prime numbers.
    """
    
    def is_prime(n):
        """
        Helper function to check if a number is prime.
        
        Parameters:
        n (int): The number to be checked.
        
        Returns:
        bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    primes = [x for x in numbers if x > 0 and is_prime(x)]
    primes.sort()
    if len(primes) >= 2:
        second_smallest = primes[1]  # second smallest prime
        second_largest = primes[-2]  # second largest prime
        return second_smallest + second_largest
    else:
        return None