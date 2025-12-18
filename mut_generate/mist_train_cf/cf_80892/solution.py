"""
QUESTION:
Create a function named `product_of_primes(n)` that calculates the product of all prime numbers less than `n`. The function should return the product of these prime numbers.
"""

def product_of_primes(n):
    def is_prime(i):
        if i <= 1:
            return False
        if i <= 3:
            return True
        if i % 2 == 0 or i % 3 == 0:
            return False
        j = 5
        while j * j <= i:
            if i % j == 0 or i % (j + 2) == 0:
                return False
            j += 6
        return True

    product = 1
    for i in range(2, n):
        if is_prime(i):
            product *= i
    return product