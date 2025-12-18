"""
QUESTION:
Create a function named `find_twin_primes` that takes an integer `n` as input and returns all twin prime pairs within the range from 2 to `n`. Implement the function with a time complexity better than O(n^2).
"""

def find_twin_primes(n):
    """
    This function finds all twin prime pairs within the range from 2 to `n`.

    Args:
    n (int): The upper limit of the range.

    Returns:
    list: A list of tuples, each containing a twin prime pair.

    """
    def sieve(n): 
        # Create a boolean array "is_prime[0..n]" and initialize all entries as True. 
        # A value in is_prime[i] will finally be False if i is Not a prime, True otherwise. 
        is_prime = [True for i in range(n+1)] 
        p = 2
        while(p * p <= n): 
            # If is_prime[p] is not changed, then it is a prime
            if (is_prime[p] == True): 
                # Update all multiples of p 
                for i in range(p * p, n+1, p): 
                    is_prime[i] = False
            p += 1
        return is_prime

    primes = sieve(n)
    twin_primes = []
    for i in range(2, len(primes)-2):
        if primes[i] and primes[i + 2]:
            twin_primes.append((i, i+2))
    return twin_primes