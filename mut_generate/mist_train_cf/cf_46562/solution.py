"""
QUESTION:
Create a function called prime_fibonacci() that takes a list of integers as input and returns a list of integers that are both prime numbers and Fibonacci numbers.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def is_perfect_square(x):
    s = int(x ** 0.5)
    return s*s == x

def is_fibonacci(n):
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def prime_fibonacci(nums):
    return [num for num in nums if is_prime(num) and is_fibonacci(num)]