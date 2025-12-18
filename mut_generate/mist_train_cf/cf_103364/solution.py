"""
QUESTION:
Create a function to print the first 100 prime numbers, where a prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The function should use a helper function to check if a number is prime.
"""

def print_first_n_primes(n):
    def is_prime(num):
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
            print(num)
            count += 1
        num += 1

def entrance():
    print_first_n_primes(100)