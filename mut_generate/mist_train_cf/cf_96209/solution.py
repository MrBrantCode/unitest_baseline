"""
QUESTION:
Write a function called `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
"""

def sum_of_primes(lst):
    def is_prime(n):
        # Check if a number is prime
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Sum up all the prime numbers in the list
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum