"""
QUESTION:
Write a function `print_prime_fibonacci` that prints the first N prime numbers in a Fibonacci series. The function should take an integer N as input and does not take any other parameters. It should only print the Fibonacci numbers that are prime, and it should stop once it has printed N prime numbers.
"""

def print_prime_fibonacci(n):
    """
    Prints the first n prime numbers in a Fibonacci series.

    Args:
    n (int): The number of prime Fibonacci numbers to print.
    """
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    a, b = 0, 1

    while count < n:
        a, b = b, a + b
        if is_prime(b):
            print(b)
            count += 1