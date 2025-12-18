"""
QUESTION:
Create a function called `find_primes` that takes two integers, `start` and `end`, as input and returns an array of prime numbers between `start` and `end` (inclusive), where `start` and `end` are the bounds of the range to search for prime numbers. The function should return all prime numbers within this range.
"""

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes