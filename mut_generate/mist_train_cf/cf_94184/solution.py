"""
QUESTION:
Implement a function `generate_fibonacci(n)` that generates a list of Fibonacci numbers up to `n`. The function should have a time complexity of O(log n) and handle the following restrictions:
- If `n` is negative, return an empty list.
- If `n` is a float or a string representation of a number, convert it to an integer before generating the Fibonacci sequence.
- If `n` is a non-integer or a string that cannot be converted to an integer, return an empty list.
- If `n` is a prime number, return an empty list.
- The function should return the Fibonacci sequence in reverse order, starting from the largest Fibonacci number and ending with the smallest.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_fibonacci(n):
    if isinstance(n, float):
        n = int(n)
    elif isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            return []
    elif not isinstance(n, int):
        return []
    
    if n < 0 or is_prime(n):
        return []
    
    fibonacci = []
    a, b = 0, 1
    while b <= n:
        fibonacci.append(b)
        a, b = b, a + b
    
    return fibonacci[::-1]