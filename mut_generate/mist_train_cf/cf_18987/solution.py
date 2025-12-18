"""
QUESTION:
Write a function `sum_of_primes` that takes a list of integers as input and returns the sum of all prime numbers in the list. The function should not take any other parameters besides the list of integers.
"""

def sum_of_primes(lst):
    def is_prime(num):
        # Check if a number is prime
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Find the sum of all prime numbers in the list
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    return prime_sum