"""
QUESTION:
Create a function called `find_prime_numbers` that takes two integers `start` and `end` as input. The function should return a list of prime numbers between `start` and `end` (inclusive), handling cases where `start` and `end` are negative, not integers, or where `start` is greater than `end`.
"""

def find_prime_numbers(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return "Input numbers must be integers"
    if start < 0 or end < 0:
        return "Input numbers must be non-negative"
    if start > end:
        return "Starting number cannot be greater than ending number"
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes