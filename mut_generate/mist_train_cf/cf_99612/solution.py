"""
QUESTION:
Write a Python function named `binary_sum` and `is_prime` to identify the first 10 prime numbers between 1 and 1000 that are also multiples of 3, print their corresponding binary representations, and calculate the sum of the digits in each binary representation. The `binary_sum` function should take a prime number as input and return the sum of its binary digits. The `is_prime` function should take a number as input and return True if it's prime, False otherwise.
"""

def binary_sum(num):
    binary = bin(num)[2:]
    return sum(int(digit) for digit in binary)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True