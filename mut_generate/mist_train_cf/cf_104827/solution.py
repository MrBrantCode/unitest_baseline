"""
QUESTION:
Write a function `sum_last_three_primes(lst)` that takes a list of integers as input, finds the last three prime numbers in the list, and returns their sum. Assume the input list contains at least three prime numbers.
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
    return sum(primes[-3:])