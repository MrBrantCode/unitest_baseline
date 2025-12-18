"""
QUESTION:
Design a function `partition_numbers()` that takes a list of numbers as input and returns three lists: one for odd numbers, one for even numbers, and one for prime numbers. The function should correctly categorize numbers that are both prime and even (i.e., the number 2), which is the only even prime number.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def partition_numbers(numbers):
    odd_numbers = []
    even_numbers = []
    prime_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        
        if is_prime(num):
            prime_numbers.append(num)

    return odd_numbers, even_numbers, prime_numbers