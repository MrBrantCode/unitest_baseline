"""
QUESTION:
Develop a function `prime_sequence(start, end)` that prints all prime numbers within a given interval defined by `start` and `end`, where `start` and `end` are integers and `start` is less than or equal to `end`. The function should use a helper function `is_prime(n)` to check if a number `n` is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_sequence(start, end):
    for num in range(start, end+1):
        if is_prime(num):
            print(num)