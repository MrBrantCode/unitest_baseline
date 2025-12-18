"""
QUESTION:
Create a function called generate_primes that takes one argument, n, representing the upper limit of the sequence. The function should generate a list of all prime numbers up to n.
"""

def generate_primes(n):
    # create a boolean list "sieve" of all numbers from 2 to n
    sieve = [True] * (n+1)
    
    # mark 0 and 1 as non-prime
    sieve[0] = sieve[1] = False
    
    # iterate over all numbers from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # if i is prime, mark all its multiples as non-prime
        if sieve[i]:
            for j in range(i**2, n+1, i):
                sieve[j] = False
    
    # return a list of all prime numbers up to n
    return [i for i in range(2, n+1) if sieve[i]]