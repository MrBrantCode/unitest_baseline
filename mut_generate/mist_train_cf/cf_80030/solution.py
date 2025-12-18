"""
QUESTION:
Write a function `product_prime_fib` that takes a list of integers as input and returns the product of the first prime number and the first Fibonacci number in the list. If the list does not contain a prime number, a Fibonacci number, or both, the function should return a corresponding message.
"""

def product_prime_fib(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_fib(n):
        if n < 0:
            return False
        x = 0
        y = 1
        while y < n:
            z = x + y
            x = y
            y = z
        return n == y or n == 0

    prime = None
    fib = None
    for num in lst:
        if prime is None and is_prime(num):
            prime = num
        if fib is None and is_fib(num):
            fib = num
        if prime is not None and fib is not None:
            return prime * fib
    return "No prime or Fibonacci number found" if prime is None and fib is None else \
           "No prime number found" if prime is None else \
           "No Fibonacci number found"