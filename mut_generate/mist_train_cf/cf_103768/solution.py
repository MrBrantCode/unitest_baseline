"""
QUESTION:
Write a function `last_three_primes` that takes a list of integers as input and returns the last three prime numbers in the list. If the list contains fewer than three prime numbers, the function should return all prime numbers in the list. Assume that the input list can be empty.
"""

def last_three_primes(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in reversed(numbers):
        if is_prime(num):
            primes.append(num)
        if len(primes) == 3:
            break
    return primes