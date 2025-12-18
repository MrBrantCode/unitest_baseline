"""
QUESTION:
Write a function `sumOfPrimes` that takes two integers `start` and `end` and returns the sum of all prime numbers within the inclusive range from `start` to `end`, where a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sumOfPrimes(start, end):
    prime_sum = 0
    for num in range(max(2, start), end + 1):
        is_prime = True
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_sum += num
    return prime_sum