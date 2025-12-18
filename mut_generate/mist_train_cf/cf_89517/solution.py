"""
QUESTION:
Implement a function named `print_square_of_primes` that takes a list of integers as input and prints the square of each prime number in the list. The function should have a time complexity of O(n√m), where n is the number of elements in the list and m is the maximum number in the list.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def print_square_of_primes(numbers):
    for num in numbers:
        if is_prime(num):
            print(num ** 2)