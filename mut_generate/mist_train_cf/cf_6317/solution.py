"""
QUESTION:
Write a function `fooBarArray` that uses recursion to generate a list of numbers from 1 to 100 (inclusive). Use a lambda function to filter out non-prime numbers and return the list of prime numbers in ascending order.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_foo_bar_array(n, result=None):
    if result is None:
        result = []
    if n > 0:
        generate_foo_bar_array(n - 1, result)
        result.append(n)
    return [x for x in result if is_prime(x)]

def fooBarArray():
    return generate_foo_bar_array(100)

print(*fooBarArray())