"""
QUESTION:
Create a function `generate_palindrome_primes()` that generates the first ten prime numbers where each prime number is a palindrome, and returns these numbers in descending order.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def generate_palindrome_primes():
    count = 0
    num = 99999
    while count < 10:
        if is_prime(num) and is_palindrome(num):
            yield num
            count += 1
        num -= 1