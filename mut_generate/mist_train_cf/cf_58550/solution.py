"""
QUESTION:
Implement a function named `find_primes` that takes two parameters, `start` and `end`, representing the start and end of a range of numbers (inclusive), and returns a list of prime numbers within this range. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Use a for loop in your implementation.
"""

def find_primes(start, end):
    primes = []

    for num in range(start, end + 1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            primes.append(num)

    return primes