"""
QUESTION:
Write a function `is_prime` and use a do-while loop structure to generate the first ten Twin Prime numbers, where a Twin Prime is a prime number that differs from another prime number by two. The function should identify and display the corresponding Twin Prime pairs.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True