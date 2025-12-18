"""
QUESTION:
Create a function named `prime_numbers(n)` that returns the first 10 prime numbers within the range from 2 to `n`. The function should use a prime number sieve algorithm to efficiently generate prime numbers.
"""

def prime_numbers(n): 
    """
    Returns the first 10 prime numbers within the range from 2 to n.
    
    Args:
    n (int): The upper limit of the range.
    
    Returns:
    list: A list of the first 10 prime numbers within the range.
    """
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
  
    prime_numbers = []
    for p in range(2, n): 
        if prime[p]: 
            prime_numbers.append(p)
    return prime_numbers[:10]