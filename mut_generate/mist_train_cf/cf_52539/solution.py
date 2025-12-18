"""
QUESTION:
Write a function `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. Use this function to find the count of elements in a list of integers that are both greater than zero and prime. The function should only consider the input list of integers and return the count of elements that meet the specified conditions.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True