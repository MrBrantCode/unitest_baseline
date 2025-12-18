"""
QUESTION:
Write a function named `smallest_prime` that takes a list of integers as input and returns the smallest prime number in the list. The list may contain up to 10,000 elements, including negative integers. If no prime numbers are found in the list, the function should return `None`.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def smallest_prime(lst):
    smallest = None
    for num in lst:
        if is_prime(num):
            if smallest is None or num < smallest:
                smallest = num
    return smallest