"""
QUESTION:
Implement a function `es_primo` that takes an integer `n` as input and returns `True` if the number is prime, and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def es_primo(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  
    return True 