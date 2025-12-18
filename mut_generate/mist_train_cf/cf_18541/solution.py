"""
QUESTION:
Write a function named `prime_numbers` that takes two integers `start` and `end` as input and returns a list of prime numbers between `start` and `end`. Assume that `start` and `end` are integers and `start` is always less than `end`. The function should have a time complexity of O(n√m), where n is the number of integers between `start` and `end`, and m is the largest number between `start` and `end`. Do not use any built-in functions or libraries to determine if a number is prime.
"""

def prime_numbers(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    if start <= 2 and end >= 2:
        primes.append(2)
    
    if start % 2 == 0:
        start += 1

    for num in range(start, end + 1, 2):
        if is_prime(num):
            primes.append(num)
    
    return primes