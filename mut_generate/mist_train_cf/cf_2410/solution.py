"""
QUESTION:
Create a function `filter_primes` that takes a list of integers as input, filters out the prime numbers, removes duplicates, and returns the prime numbers in ascending order. The function should not take any other parameters besides the list of integers.
"""

def filter_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for number in numbers:
        if is_prime(number) and number not in primes:
            primes.append(number)
    return sorted(primes)