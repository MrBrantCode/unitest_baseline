"""
QUESTION:
Develop a function `prime_product` that takes a list of integers as input and returns the product of all prime numbers in the list. Assume the input list contains only integers.
"""

def prime_product(lst):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    product = 1
    for num in lst:
        if is_prime(num):
            product *= num
    return product