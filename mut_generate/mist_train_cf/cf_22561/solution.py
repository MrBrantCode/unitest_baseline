"""
QUESTION:
Write a function `get_sorted_prime_numbers(n)` that generates a sorted list of prime numbers between 2 and `n` (exclusive), using list comprehensions and excluding non-prime numbers.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_sorted_prime_numbers(n):
    return sorted([num for num in range(2, n) if is_prime(num)])