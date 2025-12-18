"""
QUESTION:
Create a function named `find_primes(n)` that takes a positive integer `n` as input and returns a sorted list of all prime numbers up to `n` in descending order. The function should have a time complexity of O(n log log n).
"""

def find_primes(n):
    # Create a boolean array "prime[0..n]" and initialize
    # all entries it as true.
    prime = [True for _ in range(n + 1)]

    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False

    # Traverse all numbers up to sqrt(n)
    p = 2
    while p * p <= n:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Create a list of prime numbers from the boolean array
    primes = [i for i in range(n + 1) if prime[i]]
    
    # Sort the list in descending order
    primes.sort(reverse=True)

    return primes