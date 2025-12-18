"""
QUESTION:
Create a function called `is_prime(n)` that determines if a number `n` is prime and use it to find the sum of all prime numbers between 1 and 100,000 that are not palindromic. The `is_prime(n)` function should return a boolean value indicating whether `n` is prime or not. The sum of prime numbers should exclude numbers that read the same forwards and backwards (e.g., 121 or 787).
"""

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True