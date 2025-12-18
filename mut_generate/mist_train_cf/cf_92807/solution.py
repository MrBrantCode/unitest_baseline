"""
QUESTION:
Write a function `sum_first_n_primes` that takes two parameters `n` and `m` and returns the sum of the first `n` prime numbers starting with `m`. The function should iterate through numbers starting from `m` and include only prime numbers in the sum. There are no restrictions on the values of `n` and `m`.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_first_n_primes(n, m):
    prime_sum = 0
    count = 0
    current_num = m
    
    while count < n:
        if is_prime(current_num):
            prime_sum += current_num
            count += 1
        current_num += 1
    
    return prime_sum