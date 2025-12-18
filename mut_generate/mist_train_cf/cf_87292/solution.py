"""
QUESTION:
Write a function `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is prime or not. Use this function in a loop to print all prime numbers between 100 and 1000 (inclusive), and calculate their sum. The loop should iterate over the range from 100 to 1000.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True