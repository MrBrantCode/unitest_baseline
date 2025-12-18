"""
QUESTION:
Write a function named `sum_of_primes` that takes a non-empty list of integers as input and returns the sum of all prime numbers located at even index positions. A prime number has only two divisors, one and the prime number itself. The function must iterate over the list at steps of 2, starting from index 0.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(lst): 
    result = 0
    for i in range(0, len(lst), 2):
        if is_prime(lst[i]):
            result += lst[i]
    return result