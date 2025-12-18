"""
QUESTION:
Write a function `fibonacci(n)` that prints the Fibonacci series up to a given number `n`, but only includes numbers that are prime. The Fibonacci series should start with 0 and 1, and each subsequent number is the sum of the previous two. A number is prime if it is only divisible by 1 and itself. The input `n` is an integer, and the function should print the prime numbers in the Fibonacci series up to `n`.
"""

def fibonacci(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1
    while a <= n:
        if is_prime(a):
            print(a, end=' ')
        a, b = b, a + b