"""
QUESTION:
Write a function named `product_of_primes` that calculates the product of all prime numbers under a given integer `n`. The function should not use any built-in prime-checking functions or libraries. The input `n` is a positive integer. The function should optimize for time complexity.
"""

def product_of_primes(n):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))

    result = 1
    for i in range(2, n):
        if is_prime(i):
            result *= i
    return result