"""
QUESTION:
Create a function named `is_prime` that checks if a given integer `n` is a prime number using recursion. The function should return a tuple containing a boolean value indicating whether `n` is prime and the smallest prime factor of `n` if `n` is not prime. The function should start checking from `div=2` and increment by 1 in each recursive call. If `n` is less than or equal to 1, the function should return `False` and `None`. If `n` is 2, the function should return `True` and `None`. If `n` is divisible by `div`, the function should return `False` and `div`. If `div` squared is greater than `n`, the function should return `True` and `None`.
"""

def is_prime(n, div=2):
    """
    Checks if a given integer `n` is a prime number using recursion.
    
    Args:
    n (int): The number to be checked.
    div (int): The divisor to check for. Defaults to 2.
    
    Returns:
    tuple: A tuple containing a boolean value indicating whether `n` is prime and the smallest prime factor of `n` if `n` is not prime.
    """
    if n <= 1:
        return False, None
    if n == 2:
        return True, None
    if n % div == 0:
        return False, div
    if div * div > n:
        return True, None
    return is_prime(n, div + 1)