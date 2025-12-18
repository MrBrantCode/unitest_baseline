"""
QUESTION:
Design a Python generator function named `prime_gen` that takes an integer `n` (defaulting to 20) and generates prime numbers within the range of `n^2` and `2n^2`. The function should correctly identify prime numbers and adhere to the principles of prime number identification.
"""

def prime_gen(n=20):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2,int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    for num in range(n**2, 2*(n**2) + 1):
        if is_prime(num):
            yield num