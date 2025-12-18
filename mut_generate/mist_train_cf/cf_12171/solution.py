"""
QUESTION:
Write a function named `generate_prime_numbers(n)` that generates and returns the first `n` prime numbers. Assume that `n` is a positive integer. The function should not take any other parameters besides `n` and should return a list of integers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def entance(n):
    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers