"""
QUESTION:
Create a function named `sum_of_primes` that takes a single positive integer `n` as input and returns a tuple containing the sum of all prime numbers from 1 to `n` and the count of prime numbers encountered.
"""

def sum_of_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    count = 0
    sum_of_primes = 0
    for num in range(1, n+1):
        if is_prime(num):
            count += 1
            sum_of_primes += num
    return sum_of_primes, count