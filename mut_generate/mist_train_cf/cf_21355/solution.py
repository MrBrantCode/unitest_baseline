"""
QUESTION:
Create a function named `prime_with_prime_digits` that takes in two integers, `start` and `end`, and returns a list of prime numbers between `start` and `end` (inclusive). Each digit in these prime numbers must also be prime numbers. The function should only consider the digits 2, 3, 5, and 7 as prime digits, since 0 and 1 are not prime by definition, and the function does not need to check for these digits.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_with_prime_digits(start, end):
    primes = []
    for num in range(start, end + 1):
        digits = [int(d) for d in str(num)]
        if all(is_prime(d) and d in [2, 3, 5, 7] for d in digits) and is_prime(num):
            primes.append(num)
    return primes