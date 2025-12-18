"""
QUESTION:
Create a function `generate_prime_numbers(n)` that generates and returns the first `n` prime numbers. To validate the generated prime numbers, use a helper function `is_prime(num)` that checks if a given number `num` is prime. The `generate_prime_numbers` function should return a list of integers.
"""

def generate_prime_numbers(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_numbers = []
    num = 2
    while len(prime_numbers) < n:
        if is_prime(num):
            prime_numbers.append(num)
        num += 1
    return prime_numbers