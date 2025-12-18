"""
QUESTION:
Write a function `is_multiply_unique_prime(a)` that takes an integer `a` as input and returns `True` if `a` is the product of three distinct prime numbers that have not been used before in this function call, and `False` otherwise. The input `a` is guaranteed to be less than 10,000. The function should maintain a record of previously used prime numbers.
"""

used_primes = []

def is_multiply_unique_prime(a):
    global used_primes

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    factors = []
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            if is_prime(i):
                factors.append(i)
            if is_prime(a // i):
                factors.append(a // i)

    factors = list(set(factors)) 
    if len(factors) != 3: 
        return False
    else: 
        for prime in factors:
            if prime in used_primes:
                return False
        used_primes += factors 

    return True