"""
QUESTION:
Create a function `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. A prime number is defined as a number greater than 1 with no positive divisors besides 1 and itself. The function should be efficient for large numbers.
"""

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True