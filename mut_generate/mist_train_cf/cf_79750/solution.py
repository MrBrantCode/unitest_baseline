"""
QUESTION:
Write a function `strong_palindrome(n)` that takes an integer `n` as input and returns a boolean indicating whether the integer is a strong palindrome, i.e., a palindrome in at least two bases greater than 1. The function should be designed to work with integers up to `10^12`.
"""

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def convert_base(n, b):
    if n < b:
        return str(n)
    s = ""
    while n:
        s = str(n % b) + s
        n //= b
    return s

def strong_palindrome(n):
    base = 2
    while (base - 1)**2 <= n:
        if is_palindrome(convert_base(n, base)):
            if base == 2 or is_palindrome(convert_base(n, base + 1)):
                return True
        base += 1
    return False