"""
QUESTION:
Write a Python function named `find_next_prime` that takes an integer `n` as input and returns a tuple containing two values: a boolean indicating whether the input number `n` is prime, and the smallest prime number larger than `n`. The input number `n` will be a positive integer less than or equal to 10^6.
"""

def find_next_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        elif num <= 3:
            return True
        elif num % 2 == 0:
            return False
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        return True

    is_n_prime = is_prime(n)
    if is_n_prime:
        next_n = n + 1
        while True:
            if is_prime(next_n):
                return (is_n_prime, next_n)
            next_n += 1
    else:
        return (is_n_prime, n + 1)