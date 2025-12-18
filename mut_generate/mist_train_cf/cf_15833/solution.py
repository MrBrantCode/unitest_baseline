"""
QUESTION:
Write a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. The function should consider a prime number as a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sum_of_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    return sum(num for num in numbers if is_prime(num))