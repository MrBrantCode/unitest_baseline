"""
QUESTION:
Write a function `print_prime_descending(numbers)` that prints the prime numbers from the given list `numbers` in descending order without using any built-in functions or libraries and only using a constant amount of extra space. The input list can contain up to 1000 elements.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_prime_descending(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    prime_numbers.sort(reverse=True)
    for prime in prime_numbers:
        print(prime)