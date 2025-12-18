"""
QUESTION:
Create a function called `highest_prime_palindrome` that takes an integer `divisor` as input and returns the largest prime number that is a divisor of the given number and is also a palindrome. The function should return `None` if no such number exists. The input `divisor` is assumed to be an integer greater than 2.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def highest_prime_palindrome(divisor):
    for num in range(divisor - 1, 1, -1):
        if divisor % num == 0 and is_prime(num) and is_palindrome(num):
            return num
    return None