"""
QUESTION:
Create a function `is_prime(n)` that checks if a number `n` is prime or not. Write a loop that uses `is_prime(n)` to print all prime numbers from 1 to 100. Ensure the time complexity does not exceed O(n^1.5) and the space complexity does not exceed O(n).
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True