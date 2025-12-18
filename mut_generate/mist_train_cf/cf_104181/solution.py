"""
QUESTION:
Write a function to find the product of all prime numbers within a given range. The function should take a lower bound of 1000 and an upper bound of 2000. The function should return the product of all prime numbers in the range, inclusive of the bounds.
"""

def product_of_primes_in_range(lower_bound, upper_bound):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    product = 1
    for num in range(lower_bound, upper_bound + 1):
        if is_prime(num):
            product *= num
    return product