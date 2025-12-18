"""
QUESTION:
Create a program with two functions: `is_prime(n)` and `find_prime_numbers(n)`. The function `is_prime(n)` takes an integer `n` as input and returns `True` if it is a prime number and `False` otherwise. The function `find_prime_numbers(n)` takes a positive integer `n` greater than 1 as input, uses the `is_prime(n)` function to find all prime numbers under `n`, and returns them. The program should handle input validation for `n`, printing an error message and exiting if `n` is not greater than 1.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(n):
    if n <= 1:
        print("Error: n must be greater than 1")
        return

    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes