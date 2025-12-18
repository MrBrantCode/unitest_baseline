"""
QUESTION:
Create a function named `sum_of_divisors_excluding_primes` that takes a number as input and returns the sum of all its divisors excluding any divisors that are prime numbers.
"""

def sum_of_divisors_excluding_primes(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    divisors_sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            if not is_prime(i):
                divisors_sum += i
    return divisors_sum