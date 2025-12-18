"""
QUESTION:
Create a recursive function named `check_prime` that takes a number `n` and an optional parameter `i` with a default value of 2. The function should return `True` if `n` is a prime number and `False` otherwise. The function should handle exceptions where `n` is a negative number or a non-integer by returning an error message.
"""

def check_prime(n, i=2):
    # handle exceptions for negative numbers and non-integers
    if not isinstance(n, int) or n < 1:
        return "Input should be a positive integer."
        
    # base cases
    if n == 1:
        return False
    elif n == 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    # recursive case
    return check_prime(n, i + 1)