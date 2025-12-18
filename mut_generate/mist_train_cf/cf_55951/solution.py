"""
QUESTION:
Write a function `product_of_primes` that calculates the product of all prime numbers between a given range `start` and `end` (inclusive) using a helper function `is_prime` that checks if a number is prime. The function should be optimized for efficiency and should handle large products.
"""

def product_of_primes(start, end):
    def is_prime(n):
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0: return False
            i += 6
        return True

    product = 1
    for i in range(start,end + 1):
        if is_prime(i):
            product *= i
    return product