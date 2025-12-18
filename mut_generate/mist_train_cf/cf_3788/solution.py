"""
QUESTION:
Write a function called `primes_between` that takes two integers `start` and `end` as input, where `start` is always less than `end`, and returns a list of prime numbers between `start` and `end`. 

The function should have a time complexity of O(n√m), where n is the number of integers between `start` and `end`, and m is the largest number between `start` and `end`. It should not use any built-in functions or libraries that directly determine if a number is prime, handle negative integers, and minimize memory usage during computation.
"""

def primes_between(start, end):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    primes = []
    if start < 2:
        start = 2
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes