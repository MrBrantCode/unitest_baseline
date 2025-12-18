"""
QUESTION:
Create a function `fibonacci_product_primes(n)` that calculates the product of prime numbers in the Fibonacci sequence up to the nth term. The function should use a helper function `is_prime(num)` to check whether a number is prime or not. The function should return the product of prime numbers found in the sequence. Assume that when n equals 0 or 1, the product equals 1.
"""

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return False

def fibonacci_product_primes(n):
    a, b, product = 0, 1, 1 
    for i in range(n):
        if is_prime(a):
            product *= a
        a, b = b, a + b
    return product