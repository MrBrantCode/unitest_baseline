"""
QUESTION:
Design a function `find_nth_prime_fibonacci(n)` that finds the nth Fibonacci number that is also a prime number. The function should return the nth prime Fibonacci number. The input `n` is a positive integer.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime_fibonacci(n):
    count = 0
    num1, num2 = 0, 1
    while count < n:
        num1, num2 = num2, num1 + num2
        if is_prime(num2):
            count += 1
    return num2