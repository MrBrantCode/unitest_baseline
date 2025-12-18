"""
QUESTION:
Create a function called `sieve_of_eratosthenes` that takes two parameters, `start` and `end`, representing the range of numbers. The function should return a list of prime numbers within this range using the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(start, end):
    # Create a boolean array "is_prime[0..end]" and initialize
    # all entries as true.
    is_prime = [True] * (end + 1)
    
    # 0 and 1 are not prime numbers, so set their values as false.
    is_prime[0] = is_prime[1] = False
    
    # Start with the smallest prime number, 2.
    p = 2
    
    while p * p <= end:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, end + 1, p):
                is_prime[i] = False
        p += 1
    
    # Generate a list of prime numbers
    primes = []
    for i in range(start, end + 1):
        if is_prime[i]:
            primes.append(i)
    
    return primes