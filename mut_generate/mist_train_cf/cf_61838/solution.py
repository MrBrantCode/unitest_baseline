"""
QUESTION:
Write a function `check_prime_and_output(n)` that takes an integer `n` greater than or equal to 2 as input, checks if `n` is prime, and returns a tuple containing a boolean indicating whether `n` is prime and the largest prime number less than `n`. If `n` is prime, return `True` and the largest prime number less than `n`, or `True` and `None` if `n` is 2. If `n` is not prime, return `False` and the largest prime number less than `n`.
"""

def check_prime_and_output(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def largest_prime_less_than_n(num):
        for i in range(num - 1, 1, -1):
            if is_prime(i):
                return i
        return None

    prime_check = is_prime(n)
    if n == 2:
        return prime_check, None
    else:
        largest_prime = largest_prime_less_than_n(n)
        return prime_check, largest_prime