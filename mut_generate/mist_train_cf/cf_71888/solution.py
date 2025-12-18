"""
QUESTION:
Write a function `generate_fibonacci` that generates a list of Fibonacci numbers up to the input number `n`. Write another function `is_prime` that checks if a number is prime. Use these functions to determine and display all the Fibonacci prime numbers up to `n`. Do not use any predefined Python library functions. The input number `n` will not exceed 10000.
"""

def generate_fibonacci(n):
    fib_numbers = [0, 1]
    while fib_numbers[-1] + fib_numbers[-2] <= n:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return fib_numbers

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def entrance(n):
    fibonacci_numbers = generate_fibonacci(n)
    fibonacci_primes = [num for num in fibonacci_numbers if is_prime(num)]
    return fibonacci_primes