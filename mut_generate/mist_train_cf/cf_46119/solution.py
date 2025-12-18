"""
QUESTION:
Write a function that takes an array of integers as input and returns a new array containing only the prime numbers from the input array.

Function name: `get_prime_numbers` or similar, but since the provided solution uses a helper function `is_prime`, it would be best to keep the same structure. Thus, the function to be written should be named `is_prime`. 

The `is_prime` function should take an integer as input and return a boolean indicating whether the number is prime or not. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself.
"""

def is_prime(n):
    """
    Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_prime_numbers(nums):
    """
    Returns a list of prime numbers from the input list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list of prime numbers.
    """
    return [num for num in nums if is_prime(num)]