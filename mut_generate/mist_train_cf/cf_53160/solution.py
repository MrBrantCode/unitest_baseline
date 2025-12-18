"""
QUESTION:
Write a recursive function `prime_product` in Python to calculate the product of all prime numbers in a given list. Ensure the function is efficient enough to handle large lists. The function should take a list of integers as input and return the product of all prime numbers in the list.
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

    if not lst:
        return 1
    else:
        return (lst[0] * prime_product(lst[1:])) if is_prime(lst[0]) else prime_product(lst[1:])