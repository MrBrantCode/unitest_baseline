"""
QUESTION:
Write a function named `sum_of_primes` that calculates the sum of all prime numbers in a given list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. Assume the input list contains only integers.
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