"""
QUESTION:
Implement a function called `is_prime` that takes a positive integer `n` as input and returns a boolean indicating whether `n` is a prime number. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1), and it cannot use any built-in functions or libraries to determine if a number is prime.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True