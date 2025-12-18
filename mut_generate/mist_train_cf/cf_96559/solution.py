"""
QUESTION:
Write a recursive function named `print_prime_numbers` that prints the first n prime numbers, where n is a given positive integer.
"""

def is_prime(num, div=2):
    if num <= 2:
        return True if num == 2 else False
    if num % div == 0:
        return False
    if div * div > num:
        return True
    return is_prime(num, div + 1)

def print_prime_numbers(n, count=0, num=2):
    if count >= n:
        return
    if is_prime(num):
        print(num)
        count += 1
    print_prime_numbers(n, count, num + 1)