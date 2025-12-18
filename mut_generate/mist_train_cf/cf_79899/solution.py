"""
QUESTION:
Write a program that prints all prime numbers between 20 and 30 (inclusive) using a while loop. Define a helper function `is_prime(n)` that checks if a number `n` is prime. The function should return a boolean value indicating whether the number is prime or not. Use the `is_prime(n)` function within the while loop to check each number in the given range and print the prime numbers.
"""

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True