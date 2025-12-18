"""
QUESTION:
Write a function called `product_of_primes` that calculates the product of all prime numbers in a given array of integers. The function should exclude non-prime numbers from the multiplication. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def product_of_primes(array):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    product = 1
    for num in array:
        if is_prime(num):
            product *= num
    return product