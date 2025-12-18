"""
QUESTION:
Write a generator function `prime_in_range(n, start=None, end=None)` that outputs prime numbers between `n^2` and `2n^2` for a given number `n`. The function should also include optional parameters `start` and `end` to specify a range within `n^2` and `2n^2` to limit the output of prime numbers. The function should utilize a helper function `is_prime(num)` to verify that a number is prime. The time complexity of the solution should be considered.
"""

def prime_in_range(n, start=None, end=None):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    if start is None:
        start = n ** 2
    if end is None:
        end = 2 * n ** 2
    for num in range(start, end + 1):
        if is_prime(num):
            yield num