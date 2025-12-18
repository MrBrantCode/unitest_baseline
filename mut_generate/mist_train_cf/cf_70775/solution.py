"""
QUESTION:
Write a function called `find_palindrome_primes` that takes an integer `n` as input and returns a list of all palindrome prime numbers less than or equal to `n`. A palindrome prime is a number that is both a prime number and a palindrome. The function should only consider integers greater than 1 and should be able to handle large inputs.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def find_palindrome_primes(n):
    palindrome_primes = [x for x in range(2, n+1) if is_palindrome(x) and is_prime(x)]
    return palindrome_primes