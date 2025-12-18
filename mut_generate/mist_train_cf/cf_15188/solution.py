"""
QUESTION:
Write a function named `smallest_prime_factor(num)` that takes an integer `num` as input and returns its smallest prime factor. If the number itself is prime, the function should return the number itself. The function should handle numbers less than 2 by returning `None`.
"""

def smallest_prime_factor(num):
    if num < 2:
        return None
    elif num == 2:
        return 2
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return i
    
    return num