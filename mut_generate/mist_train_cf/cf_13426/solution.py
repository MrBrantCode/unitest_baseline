"""
QUESTION:
Write a program with two functions: `is_prime(num)` and `print_prime_numbers(n)`. The `is_prime(num)` function checks whether a given integer `num` is a prime number or not and returns a boolean value. The `print_prime_numbers(n)` function prints all prime numbers up to a given positive integer `n`. Assume that the input number `n` is a positive integer.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_numbers(n):
    prime_numbers = [i for i in range(2, n+1) if is_prime(i)]
    print(prime_numbers)