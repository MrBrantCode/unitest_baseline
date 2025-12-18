"""
QUESTION:
Write a function `count_prime_numbers` that takes two integers `start` and `end` as input and returns the number of prime numbers within the inclusive range from `start` to `end`.
"""

def count_prime_numbers(start: int, end: int) -> int:
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0
    for num in range(start, end + 1):
        if is_prime(num):
            count += 1
    return count