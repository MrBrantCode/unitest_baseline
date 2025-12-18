"""
QUESTION:
Create a function named `primes_between` that generates a list of distinct prime numbers between two given numbers (inclusive) and calculates their cumulative sum. The function should take two parameters: `first` and `last`, representing the range of numbers to search for primes. The function should return a list of prime numbers and their cumulative sum. The list of prime numbers should have a maximum length of 20, and the range of numbers to search for primes is between 100 and 200.
"""

def primes_between(first, last):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    primes = []
    total = 0
    for num in range(first, last + 1):
        if is_prime(num):
            primes.append(num)
            total += num
        if len(primes) == 20:
            break
    return primes, total