"""
QUESTION:
Write a function `sum_first_n_primes` that takes two parameters `n` and `m` and returns the sum of the first `n` prime numbers starting with `m`. Assume `m` is a positive integer and `n` is a non-negative integer.
"""

def sum_first_n_primes(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_sum = 0
    count = 0
    current_num = m
    
    while count < n:
        if is_prime(current_num):
            prime_sum += current_num
            count += 1
        current_num += 1
    
    return prime_sum