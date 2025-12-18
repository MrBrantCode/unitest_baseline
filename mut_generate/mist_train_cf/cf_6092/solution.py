"""
QUESTION:
Create a function called `find_primes` that takes two integers, `start` and `end`, as input and returns a list of prime numbers between `start` and `end` (inclusive). Ensure the function handles cases where `start` and `end` are negative, `start` is greater than `end`, and when the input values are not integers. Additionally, the function should handle cases where `end` is less than 2. The function should not use any built-in prime number libraries or functions.
"""

def find_primes(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return "Input integers must be integers"
    if start < 0 or end < 0:
        return "Input integers must be non-negative"
    if start > end:
        return "Starting number cannot be greater than the ending number"
    if end < 2:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes