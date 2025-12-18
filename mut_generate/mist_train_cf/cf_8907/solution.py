"""
QUESTION:
Write a function `print_prime_numbers(start, end)` that prints all prime numbers between `start` and `end` (inclusive), excluding any prime numbers that contain the digit 5.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def has_digit_5(n):
    while n > 0:
        if n % 10 == 5:
            return True
        n //= 10
    return False

def print_prime_numbers(start, end):
    for num in range(start, end + 1):
        if is_prime(num) and not has_digit_5(num):
            print(num)