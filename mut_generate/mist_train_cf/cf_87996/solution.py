"""
QUESTION:
Write a function `sum_first_100_primes` that takes an array of integers as input and returns the sum of the first 100 prime numbers in the array. The input array contains at least 100 prime numbers and at most 1000 elements.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_first_100_primes(arr):
    primes_sum = 0
    count = 0

    for num in arr:
        if is_prime(num):
            primes_sum += num
            count += 1
            if count == 100:
                break

    return primes_sum