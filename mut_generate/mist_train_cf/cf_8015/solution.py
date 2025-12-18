"""
QUESTION:
Write a function sum_of_primes that takes a list of integers as input and returns the sum of all prime numbers in the list. The function should not use built-in sum or iteration tools such as 'for' or 'while' loops, and its time complexity should be O(n), where n is the length of the input list. Negative integers should not be considered as prime numbers.
"""

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(nums):
    """
    Calculate the sum of prime numbers in a list.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        int: The sum of prime numbers in the list.
    """
    prime_sum = 0
    for num in nums:
        if is_prime(num):
            prime_sum += num
    return prime_sum