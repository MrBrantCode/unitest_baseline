"""
QUESTION:
Create a function named `is_prime` that checks if a number is prime. Then, write a while loop that increments a counter by 1 starting from 0 until it reaches a prime number. The loop should break as soon as it encounters a prime number. The counter should not exceed 100.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True