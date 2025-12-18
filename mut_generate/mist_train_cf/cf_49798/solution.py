"""
QUESTION:
Write a function called `is_prime(n)` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. The function should use a while loop to check for primality. The input `n` is an integer greater than 0.
"""

def entrance(n):
    if n <= 1:
        return False
    elif n <=3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while(i * i <= n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True