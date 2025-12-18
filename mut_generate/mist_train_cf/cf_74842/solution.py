"""
QUESTION:
Write a function `prime_product` that takes an integer `num` and returns a tuple of 2 or 3 distinct prime factors if `num` can be represented as the product of 2 or 3 unique prime numbers, and returns 'Not a product of unique prime numbers.' otherwise. The input `num` is less than 10,000.
"""

def is_prime(n):
    if n < 2: 
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_product(num):
    factors = []
    for i in range(2, num):
        while num % i == 0:
            factors.append(i)
            num = num / i
            if num == 1 or len(factors) > 3 or (len(factors) == 3 and i == factors[-2]):
                return 'Not a product of unique prime numbers.'
    if len([i for i in factors if is_prime(i)]) in (2, 3): 
        return tuple(factors)
    else:
        return 'Not a product of unique prime numbers.'