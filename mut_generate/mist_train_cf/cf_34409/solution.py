"""
QUESTION:
Create a function `count_primes` that takes a list of integers as input and returns the count of prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should be efficient to handle large input lists. The function should only count prime numbers and exclude non-prime numbers and numbers less than or equal to 1.
"""

def count_primes(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count