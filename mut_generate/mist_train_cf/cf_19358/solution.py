"""
QUESTION:
Create a function `prime_list` that generates a list of prime numbers from `m` to `n` (inclusive), where both `m` and `n` are positive integers greater than 1. Each prime number in the list should be repeated twice.
"""

def prime_list(m, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_nums = [num for num in range(m, n + 1) if is_prime(num)]
    return [num for num in prime_nums for _ in range(2)]