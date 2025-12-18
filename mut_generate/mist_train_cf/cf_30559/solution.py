"""
QUESTION:
Implement a function `sumOfPrimes(start, end)` that calculates the sum of all prime numbers within the inclusive range from `start` to `end`, where `start` and `end` are positive integers and `start` is less than or equal to `end`. The function should return the sum of all prime numbers within the given range.
"""

def sumOfPrimes(start: int, end: int) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum