"""
QUESTION:
Create a function named `prime_generator` that takes an integer `n` as input and generates prime numbers in the range of `n` squared (`n * n`) to twice the square of `n` (`2 * n * n`).
"""

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5)+1, 2):
            if number % i == 0:
                return False
        return True
    return False

def prime_generator(n):
    for number in range(n * n, 2 * n * n + 1):
        if is_prime(number):
            yield number