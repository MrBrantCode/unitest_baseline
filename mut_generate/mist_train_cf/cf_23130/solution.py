"""
QUESTION:
Write a function called `sum_of_first_n_primes` that calculates the sum of the first n prime numbers. The function takes one integer argument `n` and returns the sum of the first n prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_first_n_primes(n):
    sum_of_primes = 0
    count = 0
    current_num = 2
    
    while count < n:
        if is_prime(current_num):
            sum_of_primes += current_num
            count += 1
        current_num += 1
    
    return sum_of_primes