"""
QUESTION:
Create a function named `sum_of_primes` that takes an integer `num` as input. The function should calculate the sum of all prime numbers smaller than or equal to `num`. The function should return the calculated sum.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_of_primes(num):
    prime_sum = 0
    for i in range(2, num + 1):
        if is_prime(i):
            prime_sum += i
    return prime_sum