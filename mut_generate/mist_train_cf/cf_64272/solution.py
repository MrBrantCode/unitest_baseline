"""
QUESTION:
Write a function `prime_number_seive(n)` and `prime_factors(n)` to find all prime numbers up to a given number `n` and their prime factors respectively. The `prime_number_seive(n)` function should return a list of prime numbers up to `n`, and the `prime_factors(n)` function should return a list of prime factors of `n`. The function should also be able to determine the number of unique prime factors of `n` if `n` itself is a prime number. The input `n` is a positive integer.
"""

def prime_number_seive(n):
    """
    Returns a list of prime numbers up to n.
    
    Parameters:
    n (int): A positive integer.
    
    Returns:
    list: A list of prime numbers up to n.
    """
    prime = [True for _ in range(n+1)]
    sieve = []
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            sieve.append(p)
    return sieve

def prime_factors(n):
    """
    Returns a list of prime factors of n.
    
    Parameters:
    n (int): A positive integer.
    
    Returns:
    list: A list of prime factors of n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors