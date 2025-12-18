"""
QUESTION:
Write a function `cubes_of_primes(n)` that calculates and prints the cubes of all prime numbers between 1 and `n` (inclusive), where `n` is a positive integer. The function should not take any input other than `n` and should not return any value. The function should be able to handle any positive integer `n`.
"""

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    i = 3
    while i * i <= num:
        if num % i:
            i += 2
        else:
            return False
    return True

def cubes_of_primes(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(f'{num}: {num**3}')