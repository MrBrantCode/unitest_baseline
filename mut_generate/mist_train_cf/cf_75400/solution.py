"""
QUESTION:
Write a function named `is_prime(n)` that determines whether a given integer `n` is prime or not, using the Sieve of Eratosthenes algorithm. The function should return `True` for prime numbers and `False` for non-prime numbers. The input `n` is a non-negative integer. The function should handle cases where `n` is less than or equal to 1.
"""

def is_prime(n):
    """Return True if n is a prime number, False if not.

    Checks for primality by creating a boolean array "prime[0..n]" 
    and initialize all entries as true. 

    A value in prime[i] will finally be false if i is Not a prime, 
    otherwise, true bool value.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    prime[0], prime[1] = False, False
    p = 2
    while(p*p<=n):
        # If prime[p] is not changed, then it is a prime
        if(prime[p]==True):
            # Update all multiples of p
            for i in range(p*p,n+1,p):
                prime[i] = False
        p += 1
    # Return the primality check result for n
    return prime[n]