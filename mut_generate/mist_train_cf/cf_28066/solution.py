"""
QUESTION:
Implement the `is_prime` function, which takes an integer `n` as input and returns `True` if `n` is prime, and `False` otherwise. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should not use any external libraries or classes, and it should be efficient for large inputs.
"""

def is_prime(n):
    if n <= 1:
        return False  

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  

    return True  