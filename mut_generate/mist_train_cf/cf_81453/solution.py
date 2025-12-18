"""
QUESTION:
Write a function `prime_triplet_product(a)` that takes an integer `a` as input and returns a tuple of three distinct prime numbers if `a` is the direct product of three unique prime numbers, otherwise returns 'Not a product of 3 distinct prime numbers.' The input `a` must be less than 1000.
"""

def prime_triplet_product(a):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n%i == 0 or n%(i + 2) == 0:
                return False
            i += 6
        return True

    if a > 998001 or a < 6:
        return 'Not a product of 3 distinct prime numbers.'
    primes = []
    
    for possible_factor in range(2, a):
        if a % possible_factor == 0 and is_prime(possible_factor):
            primes.append(possible_factor)
            a = a // possible_factor

        if len(primes) > 3:
            return 'Not a product of 3 distinct prime numbers.'
    if a > 1 and is_prime(a) and a not in primes:
        primes.append(a)

    if len(primes) == 3:
        return tuple(primes)
        
    return 'Not a product of 3 distinct prime numbers.'