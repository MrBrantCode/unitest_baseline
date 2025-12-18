"""
QUESTION:
Create a function that generates a continuous series of prime integers within a given range, with the function name `is_prime(n)` and a range of 20 to 50. The function should return `True` if a number is prime and `False` otherwise, and use a loop to print all prime numbers within the specified range.
"""

def is_prime(n):
    """function to check if the number is prime or not"""
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