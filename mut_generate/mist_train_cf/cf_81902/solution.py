"""
QUESTION:
Implement a recursive function `primes_up_to_n` to find all prime numbers up to a given number `n` without using any built-in or external libraries. The function should take two additional parameters: `candidate` (default value of 2) and `primes` (default value of an empty list). Optimize the function for large values of `n`. The function should not exceed Python's recursion depth limit for very large values of `n`.
"""

def primes_up_to_n(n, candidate=2, primes=[]):
    """
    This function finds all prime numbers up to a given number n.
    
    Parameters:
    n (int): The upper limit for finding prime numbers.
    candidate (int): The current number being checked for primality. Default is 2.
    primes (list): A list of prime numbers found so far. Default is an empty list.
    
    Returns:
    list: A list of all prime numbers up to n.
    """
    # Base case
    if candidate > n: 
        return primes
    
    # Checking if the candidate is prime
    elif all(candidate % p != 0 for p in primes): 
        return primes_up_to_n(n, candidate + 1, primes + [candidate])
    else:
        return primes_up_to_n(n, candidate + 1, primes)