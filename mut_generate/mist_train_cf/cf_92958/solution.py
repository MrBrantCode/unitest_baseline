"""
QUESTION:
Design a function `all_primes(numbers)` that takes a list of numbers as input and returns `True` if all numbers in the list are prime, and `False` otherwise. The function should handle numbers less than or equal to 1 and non-integer inputs.
"""

def all_primes(numbers):
    def is_prime(n):
        if n <= 1 or not isinstance(n, int):
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in numbers:
        if not is_prime(num):
            return False
    return True