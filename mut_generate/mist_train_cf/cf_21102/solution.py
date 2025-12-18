"""
QUESTION:
Create a function `nth_prime(n)` that takes an integer `n` as input and returns the `n`th prime number. The function should efficiently calculate prime numbers without using any pre-calculated lists or libraries.
"""

def nth_prime(n):
    primes = []
    num = 2  # Start with the first prime number
    
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
        num += 1
    
    return primes[-1]  # Return the last prime number in the list