"""
QUESTION:
Design a function `find_nth_prime_fibonacci(n)` that finds the nth Fibonacci number that is also a prime number. The function should take an integer `n` as input, where `n` is a positive integer greater than 0. The function should return the nth Fibonacci number that is also a prime number.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_nth_prime_fibonacci(n):
    """
    Finds the nth Fibonacci number that is also a prime number.

    Args:
    n (int): A positive integer greater than 0.

    Returns:
    int: The nth Fibonacci number that is also a prime number.
    """
    count = 0
    num1, num2 = 0, 1
    while count < n:
        fib_num = num1 + num2
        if is_prime(fib_num):
            count += 1
        num1, num2 = num2, fib_num
    return num2