"""
QUESTION:
Write a function `is_prime()` to check if a number is prime or not. Using this function, print all prime numbers from a given list in ascending order. The solution should have a time complexity of O(n) and should not use any built-in Python functions, additional data structures, or variables apart from the given list.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True