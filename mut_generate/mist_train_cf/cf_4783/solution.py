"""
QUESTION:
Write a function named `prime_fibonacci_numbers` to print the first 500 numbers that are both prime and Fibonacci numbers. The function should not take any arguments.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def prime_fibonacci_numbers():
    count = 0
    number = 2
    while count < 500:
        if is_prime(number) and is_fibonacci(number):
            print(number)
            count += 1
        number += 1