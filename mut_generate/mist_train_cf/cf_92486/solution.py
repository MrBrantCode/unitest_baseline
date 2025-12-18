"""
QUESTION:
Write a function named `sum_of_primes` that takes a list of integers as input and returns the sum of the prime numbers in the list. The function should handle a list of any size and content.
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