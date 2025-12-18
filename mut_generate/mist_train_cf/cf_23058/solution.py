"""
QUESTION:
Write a function `largest_prime_in_string` that takes a string `input_string` as input and returns the largest single-digit prime number found in the string. If no prime numbers are found, return `None`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should only consider single-digit prime numbers (i.e., 2, 3, 5, 7).
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_in_string(input_string):
    largest_prime = None
    for char in input_string:
        if char.isdigit():
            num = int(char)
            if is_prime(num):
                if largest_prime is None or num > largest_prime:
                    largest_prime = num
    return largest_prime