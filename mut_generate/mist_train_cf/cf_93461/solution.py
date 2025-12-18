"""
QUESTION:
Create a function `contains_only_primes` that takes a string of space-separated integers as input and returns `True` if all the numbers are prime, and `False` otherwise. The input string will only contain non-negative integers separated by spaces.
"""

def contains_only_primes(string):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    numbers = string.split()
    for number in numbers:
        if not is_prime(int(number)):
            return False
    return True