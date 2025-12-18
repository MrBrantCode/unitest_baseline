"""
QUESTION:
Write a recursive function named `print_prime_sum` that calculates the sum of all odd integers up to `n` (inclusive) and prints the sum only if it's a prime number. The function should take an integer `n` as input, where `n` is between 100 and 1000 (inclusive). Ensure the function handles the case when `n` is even by subtracting 1 from `n` before calculating the sum.
"""

def print_prime_sum(n):
    def recursive_sum(n):
        if n <= 1:
            return n
        return n + recursive_sum(n - 2)

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(n**0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return False
        return True

    if n % 2 == 0:
        n -= 1
    total = recursive_sum(n)
    if is_prime(total):
        print(total)