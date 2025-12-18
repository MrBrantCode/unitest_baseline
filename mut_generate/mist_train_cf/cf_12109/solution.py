"""
QUESTION:
Create a function `is_prime_palindrome(num)` that takes an integer as input and returns `True` if the number is both prime and a palindrome, and `False` otherwise. The function should not take any additional parameters.
"""

def is_prime_palindrome(num):
    if num < 2:
        return False

    def is_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    return is_prime(num) and is_palindrome(num)