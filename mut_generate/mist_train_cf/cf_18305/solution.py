"""
QUESTION:
Create a function `generate_prime_fibonacci(n)` that generates a list of the first `n` prime Fibonacci numbers. A prime Fibonacci number is a Fibonacci number that is prime. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should return a list of integers.
"""

import math

def generate_prime_fibonacci(n):
    """
    Generate a list of the first n prime Fibonacci numbers.

    Args:
        n (int): The number of prime Fibonacci numbers to generate.

    Returns:
        list: A list of the first n prime Fibonacci numbers.
    """
    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        
        max_divisor = math.isqrt(num) + 1
        for divisor in range(3, max_divisor, 2):
            if num % divisor == 0:
                return False
        return True

    prime_fibonacci_list = []
    a, b = 0, 1
    while len(prime_fibonacci_list) < n:
        a, b = b, a + b
        if is_prime(a):
            prime_fibonacci_list.append(a)
    
    return prime_fibonacci_list