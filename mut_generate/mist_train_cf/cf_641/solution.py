"""
QUESTION:
Write a function, `prime_fibonacci_numbers`, that prints all prime numbers from 1 to 1000 that are also Fibonacci numbers. 

The function should use two helper functions: `is_prime(n)` to check if a number `n` is prime, and `is_fibonacci(n)` to check if a number `n` is a Fibonacci number. 

Note that a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. A Fibonacci number is a number in the sequence where a number is the addition of the last two numbers, starting with 0 and 1.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_fibonacci(n):
    if n < 0:
        return False
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def prime_fibonacci_numbers():
    for num in range(1, 1001):
        if is_prime(num) and is_fibonacci(num):
            print(num)