"""
QUESTION:
Write a function `find_second_smallest_odd_prime` that takes an array of positive integers as input and returns the second smallest odd prime number greater than 10 in the array. If no such number exists, return a message or value indicating that.
"""

def find_second_smallest_odd_prime(nums):
    """
    This function finds the second smallest odd prime number greater than 10 in the given list of numbers.

    Args:
        nums (list): A list of positive integers.

    Returns:
        int or str: The second smallest odd prime number greater than 10 if found, otherwise "Not Found".
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    odd_primes = [num for num in nums if num > 10 and num % 2 != 0 and is_prime(num)]
    odd_primes.sort()

    if len(odd_primes) < 2:
        return "Not Found"
    else:
        return odd_primes[1]