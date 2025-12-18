"""
QUESTION:
Write a function `is_prime` to check if a number is prime and another function `product_of_primes` to calculate the product of all prime numbers under a given number `n`. The function `product_of_primes` should take an integer `n` as input and return the product of all prime numbers less than `n`.
"""

def product_of_primes(n):
    def is_prime(x):
        if x == 1:
            return False
        elif x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True

    product = 1
    for i in range(2, n):
        if is_prime(i):
            product *= i
    return product