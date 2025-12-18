"""
QUESTION:
Write a function named `sum_of_primes(a, b)` that takes a range of numbers [a, b] as input and returns the sum of all prime numbers within that range. The function should check each number in the range to determine if it is prime and add it to the sum if it is.
"""

def is_prime(num):
    # 0 and 1 are not prime
    if num < 2:
        return False
    
    # Check for factors up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def sum_of_primes(a, b):
    prime_sum = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum