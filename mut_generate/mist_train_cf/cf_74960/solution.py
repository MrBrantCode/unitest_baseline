"""
QUESTION:
Create a function called `sum_primes(x, y)` that calculates the sum of all prime numbers between `x` and `y`, inclusive of `x` but not `y`. The input values are restricted to 1 <= x < y <= 10^4.
"""

def sum_primes(x, y):
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

    prime_sum = 0
    for n in range(x, y):
        if is_prime(n):
            prime_sum += n
    return prime_sum