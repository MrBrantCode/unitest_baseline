"""
QUESTION:
Design a function in Python named `all_primes` that takes a list of numbers as input and returns `True` if all numbers in the list are prime, and `False` otherwise. Assume that the input list contains only integers.
"""

def all_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if not is_prime(num):
            return False
    return True