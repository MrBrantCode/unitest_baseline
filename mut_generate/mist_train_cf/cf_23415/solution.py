"""
QUESTION:
Write a function named `generate_primes` that returns a list of all prime numbers within a specified range, excluding 1 and 2. The function should take two parameters: `start` and `end`, representing the start and end of the range, respectively. The function should return a list of prime numbers.
"""

def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 2 and all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return primes