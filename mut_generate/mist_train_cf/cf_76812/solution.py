"""
QUESTION:
Create a function `fibo_primes_sum(n)` that calculates the sum of the Fibonacci series up to the nth term, including only prime numbers. The function should take an integer `n` as input and return the sum of prime Fibonacci numbers. Note that achieving a time complexity of O(log n) for this problem is intractable with current algorithms due to the prime number check, which has a higher time complexity.
"""

def fibo_primes_sum(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if n < 1:
        return 0

    f1, f2, i, sum = 0, 1, 1, 0
    while i <= n:
        if is_prime(f2):
            sum = sum + f2
        f1, f2 = f2, f1 + f2
        i += 1
    return sum