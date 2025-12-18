"""
QUESTION:
Design a function `is_prime_palindromic(n)` to check if a number is both prime and palindromic, and use this function to print out all the prime palindromic numbers between 1 and 100 (inclusive). The input number `n` should be an integer, and the output should be a boolean value (True if `n` is both prime and palindromic, False otherwise).
"""

def is_prime_palindromic(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return str(n) == str(n)[::-1]