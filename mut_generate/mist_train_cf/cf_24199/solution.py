"""
QUESTION:
Write a function `find_next_prime` that takes an integer `n` as input and returns the first prime number larger than `n`. Assume `n` is a positive integer.
"""

def find_next_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    num = n + 1
    while not is_prime(num):
        num += 1
    return num