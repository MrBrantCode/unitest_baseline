"""
QUESTION:
Write a function named `custom_loop` that takes a list of integers as input and iterates through the list in reverse order. The function should only iterate through even numbers in the list and terminate if it encounters a prime number. If the function encounters a prime number, it should continue iterating only if the next element is a perfect square.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    return math.isqrt(n)**2 == n

def custom_loop(lst):
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] % 2 == 0:
            if is_prime(lst[i]):
                break
            if i > 0 and is_perfect_square(lst[i - 1]):
                print(lst[i])