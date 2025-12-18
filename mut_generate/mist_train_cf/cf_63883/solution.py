"""
QUESTION:
Write a function `check_prime(n)` that determines if a given integer `n` is prime. The function should return `True` if the number is prime and `False` otherwise. The function should have a time complexity of O(sqrt(n)) and use minimal extra space. The input `n` can be any integer.
"""

def check_prime(n):
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
        i = i + 6
    return True