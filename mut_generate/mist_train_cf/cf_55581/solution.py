"""
QUESTION:
Construct a function `fib_dict` that generates a dictionary where keys are the first 25 terms of the Fibonacci sequence and values are either tuples or dictionaries. If a Fibonacci term is a prime number, the value should be a dictionary with keys 'sqrt' and 'square' representing the square root and square of the term respectively. If the Fibonacci term is not a prime number, the value should be a tuple containing the square root and square of the term. The function should use efficient memory management by generating Fibonacci numbers one by one instead of storing the entire sequence in memory.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_dict():
    return {
        term: ({'sqrt': math.sqrt(term), 'square': term**2} if is_prime(term) else (math.sqrt(term), term**2))
        for idx, term in enumerate(fibonacci(25), start=1) if term > 0
    }