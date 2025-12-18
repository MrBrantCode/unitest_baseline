"""
QUESTION:
Write a function to print the first 100 prime numbers. The function should check each number sequentially starting from 2 to determine if it is a prime number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should use a helper function to check if a number is prime.
"""

def print_primes(n):
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False

        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2

    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1