"""
QUESTION:
Create two functions: `factorial(x)` that calculates the factorial of `x` using recursion, and `find_nth_prime(n)` that finds the `n`th prime number. `n` represents the index of the prime number to be found.
"""

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

def find_nth_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes[-1]