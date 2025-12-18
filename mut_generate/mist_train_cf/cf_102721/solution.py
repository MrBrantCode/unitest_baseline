"""
QUESTION:
Write a function named `find_primes` that takes a list of integers as input and returns a list of prime numbers from the input list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should not include 1 in the output, even if it is present in the input list. The function should be implemented using a lambda function and the `filter()` function.
"""

def find_primes(nums):
    """
    Returns a list of prime numbers from the input list.
    
    Args:
    nums (list): A list of integers.
    
    Returns:
    list: A list of prime numbers.
    """
    return list(filter(lambda num: all(num % i != 0 for i in range(2, int(num**0.5)+1)) and num > 1, nums))