"""
QUESTION:
Create a function `filter_primes` that takes a list of integers as input and returns a new list containing only the prime numbers greater than 3 from the original list. The function should not modify the original list.
"""

def filter_primes(nums):
    """
    Returns a new list containing only the prime numbers greater than 3 from the input list.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A new list containing only the prime numbers greater than 3.
    """
    def is_prime(num):
        if num <= 3:
            return False
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True

    return [num for num in nums if is_prime(num)]