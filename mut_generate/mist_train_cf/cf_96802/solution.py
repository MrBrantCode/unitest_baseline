"""
QUESTION:
Write a function named `sum_last_three_primes` that takes a list of integers as input and returns the sum of the last three prime numbers in the list. If there are less than three prime numbers, return the sum of all prime numbers. Assume the input list contains at least one prime number.
"""

def sum_last_three_primes(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in lst if is_prime(num)]
    last_three_primes = primes[-3:]
    return sum(last_three_primes)