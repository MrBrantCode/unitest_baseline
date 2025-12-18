"""
QUESTION:
Design a function named `separate_numbers` that takes a list of positive integers as input and returns two lists, one containing the prime numbers and the other containing the composite numbers.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def separate_numbers(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    composite_numbers = [num for num in numbers if not is_prime(num)]
    return prime_numbers, composite_numbers