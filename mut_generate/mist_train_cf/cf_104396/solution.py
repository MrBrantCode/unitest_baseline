"""
QUESTION:
Write a function named `count_prime_numbers` that takes two integers, `start` and `end`, as input and returns the number of prime numbers within the given range (inclusive). The function should not include any number less than 2 in its count, as it is not a prime number.
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