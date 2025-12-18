"""
QUESTION:
Create a function `is_emirp` that determines whether a given number is an emirp number, which is a non-palindromic prime number whose reverse is also a prime number. The function should have a time complexity less than O(n^2).
"""

import math

def is_emirp(n):
    if n <= 1:
        return False

    # Emirp numbers are not palindromic, so we can exit early if it's a palindrome.
    if str(n) == str(n)[::-1]:
        return False

    # Check if a number is prime or not
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        sqrt_num = math.isqrt(num)
        for i in range(3, sqrt_num + 1, 2):
            if num % i == 0:
                return False
        return True

    # If number is prime and its reverse is also prime then it is emirp
    if is_prime(n) and is_prime(int(str(n)[::-1])):
        return True

    return False