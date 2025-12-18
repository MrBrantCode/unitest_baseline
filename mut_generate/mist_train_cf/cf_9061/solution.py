"""
QUESTION:
Write a function called `sum_of_primes` that takes an array of integers as input and returns the sum of all the prime numbers in the array.
"""

def sum_of_primes(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return sum(num for num in numbers if is_prime(num))