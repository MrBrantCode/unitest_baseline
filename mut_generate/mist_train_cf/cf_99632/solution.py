"""
QUESTION:
Write a function `prime_product(lst)` that calculates the product of all prime numbers in a given list of integers `lst`. The function should return the product as an integer.
"""

def prime_product(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    product = 1
    for num in lst:
        if is_prime(num):
            product *= num
    return product