"""
QUESTION:
Create a function called `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. Then, write another function that uses `is_prime` to calculate the sum of the first 1000 prime numbers. The function should start checking from the first prime number and should not include non-prime numbers in the count.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def sum_of_first_n_primes(n):
    count = 0
    sum_of_primes = 0
    num = 2  # Start with the first prime number

    while count < n:
        if is_prime(num):
            sum_of_primes += num
            count += 1
        num += 1

    return sum_of_primes