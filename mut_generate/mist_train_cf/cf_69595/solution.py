"""
QUESTION:
Write a function `get_palindrome_primes(n)` and `get_next_palindrome_primes(n, count)` to identify all palindrome prime numbers less than or equal to a specified number `n` and generate an array of the next `count` palindromic primes following the given number `n`. Do not use any library functions for palindrome check or prime number identification. The implementation should limit its time complexity to less than O(n^2).
"""

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_palindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def get_palindrome_primes(n):
    """Get all palindrome prime numbers less than or equal to n."""
    return [i for i in range(2, n+1) if is_palindrome(i) and is_prime(i)]

def get_next_palindrome_primes(n, count):
    """Get the next count palindromic primes following the given number n."""
    primes = []
    i = n + 1
    while len(primes) < count:
        if is_palindrome(i) and is_prime(i):
            primes.append(i)
        i += 1
    return primes