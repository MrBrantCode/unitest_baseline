"""
QUESTION:
Construct a function named `sieve_of_eratosthenes` that identifies and lists all prime numbers within a specified range. The function should take two parameters: `n`, the upper limit of the range, and `m`, the lower limit of the range (default value is 2). Implement the Sieve of Eratosthenes algorithm and return a list of all prime numbers between `m` and `n` (inclusive).
"""

def sieve_of_eratosthenes(n, m=2):
    """
    This function implements the Sieve of Eratosthenes algorithm to find all prime numbers within a specified range.
    
    Parameters:
    n (int): The upper limit of the range (inclusive).
    m (int): The lower limit of the range (inclusive). Default is 2.
    
    Returns:
    list: A list of all prime numbers between m and n (inclusive).
    """
    
    # Initialize a boolean array prime of size n+1 with all entries as true.
    prime = [True] * (n + 1)
    
    # 0 and 1 are not prime numbers
    prime[0] = prime[1] = False
    
    # Iterate over each number starting from 2 to sqrt(n)
    for p in range(2, int(n ** 0.5) + 1):
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p to be not prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
    
    # Return a list of all prime numbers between m and n (inclusive)
    return [p for p in range(max(m, 2), n + 1) if prime[p]]