"""
QUESTION:
Write a function named `group_primes(numbers)` that takes a list of integers as input and returns a dictionary where the keys are prime numbers from the input list and the values are lists of their occurrences. The function should consider the absolute values of the numbers when checking for primality.
"""

def group_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = {}
    for num in numbers:
        if is_prime(abs(num)):
            if num not in primes:
                primes[num] = []
            primes[num].append(num)
    return primes