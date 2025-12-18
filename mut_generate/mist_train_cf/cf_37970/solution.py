"""
QUESTION:
Implement a function named `sumOfPrimes` that takes two integers, `start` and `end`, as input and returns the sum of all prime numbers within the inclusive range from `start` to `end`. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sumOfPrimes(start, end):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    for num in range(start, end + 1):
        if isPrime(num):
            prime_sum += num
    return prime_sum