"""
QUESTION:
Implement a function `sum_of_primes` that takes two integers `start` and `end` as input and returns the sum of all prime numbers within the inclusive range from `start` to `end`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be able to handle any valid range of integers and return the correct sum.
"""

def sum_of_primes(start: int, end: int) -> int:
    prime_sum = 0
    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    return prime_sum