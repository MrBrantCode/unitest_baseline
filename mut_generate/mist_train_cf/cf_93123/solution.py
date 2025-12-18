"""
QUESTION:
Create a function `sum_of_primes_up_to(n)` that calculates the sum of all prime numbers up to a given number `n`. The function should iterate through each number up to `n` and check if it is prime, adding it to a running total if it is.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes_up_to(n):
    sum_of_primes = 0
    for num in range(2, n + 1):
        if is_prime(num):
            sum_of_primes += num
    return sum_of_primes