"""
QUESTION:
Write a function `highest_prime_palindrome(divisor)` that finds and returns the highest prime number that can be divided by `divisor` and is also a palindrome. The function should start checking from `divisor - 1` and work downwards. If no such prime palindrome is found, return `None`.
"""

def highest_prime_palindrome(divisor):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    for num in range(divisor - 1, 1, -1):
        if divisor % num == 0 and is_prime(num) and is_palindrome(num):
            return num
    return None