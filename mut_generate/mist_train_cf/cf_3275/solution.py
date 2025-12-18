"""
QUESTION:
Write a function named `is_prime` that checks if a number is prime. Then, using this function, add all prime numbers between 0 and 10,000 (inclusive) to a given list `my_list`. Ensure that the `is_prime` function has a time complexity better than O(n).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True