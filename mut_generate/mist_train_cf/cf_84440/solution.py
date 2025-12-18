"""
QUESTION:
Write a function `fib_primes(n)` that generates a list of prime numbers from a Fibonacci sequence up to a given input number `n`. The function should return a list of prime numbers only.
"""

def fib_primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    fib_prime_list = []
    a, b = 0, 1
    while a <= n:
        if is_prime(a):
            fib_prime_list.append(a)
        a, b = b, a + b
    
    return fib_prime_list