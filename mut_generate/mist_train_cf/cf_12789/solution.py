"""
QUESTION:
Write a function named `sum_of_primes` that takes a list of integers as input and returns the sum of the prime numbers in the list. The function should define a helper function `is_prime` to check if a number is prime. The list may contain any integers, including negative numbers and zeros.
"""

def sum_of_primes(lst):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    prime_sum = 0
    for num in lst:
        if is_prime(num):
            prime_sum += num
    
    return prime_sum