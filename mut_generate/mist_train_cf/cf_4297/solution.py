"""
QUESTION:
Write a recursive function named "sum_of_primes" that takes two parameters: "start" and "end", representing the range of numbers to consider. The function should return the sum of all prime numbers within the given range. You are not allowed to use any external libraries or built-in functions to check for prime numbers. You can define additional helper functions if needed.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    if start > end:
        return 0
    elif is_prime(start):
        return start + sum_of_primes(start + 1, end)
    else:
        return sum_of_primes(start + 1, end)