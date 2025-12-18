"""
QUESTION:
Write a function `sumOfPrimes` that takes two integers `start` and `end` as input and returns the sum of all prime numbers between `start` and `end`, inclusive. The function should only consider natural numbers greater than 1 that have no positive divisors other than 1 and themselves as prime numbers. The function signature is `def sumOfPrimes(start: int, end: int) -> int:`
"""

def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sumOfPrimes(start: int, end: int) -> int:
    prime_sum = 0
    for num in range(max(2, start), end + 1):
        if isPrime(num):
            prime_sum += num
    return prime_sum