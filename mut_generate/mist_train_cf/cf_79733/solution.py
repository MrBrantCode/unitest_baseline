"""
QUESTION:
Create a function `sieve_of_eratosthenes(n)` that takes an integer `n` as input and returns a list of all prime numbers less than `n`. Implement the function using the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(n):
    # Create a boolean array "prime[0:n+1]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
  
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
  
            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1 
  
    # Return all prime numbers
    return [p for p in range(2, n) if prime[p]]