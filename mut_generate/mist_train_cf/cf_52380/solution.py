"""
QUESTION:
Write a function `sieve_of_eratosthenes(n)` that generates all prime numbers between 100 and `n`, where `n` is a given number up to 10^7. The function should be efficient for larger ranges and have a time complexity of O(n log log n).
"""

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize all entries it as true.
    # A value in prime[i] will finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while p * p <= n:
 
        # If prime[p] is not changed, then it is a prime
        if prime[p] is True:
 
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
 
    # Return the primes from the range 100 to n
    return [p for p in range(100, n) if prime[p]]