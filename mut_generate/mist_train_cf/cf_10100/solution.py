"""
QUESTION:
Create a function named `filter_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The input list will contain integers greater than or equal to 1.
"""

def filter_prime_numbers(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]