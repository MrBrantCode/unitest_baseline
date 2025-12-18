"""
QUESTION:
Write a function `product_of_factorials` that calculates the product of the results when a factorial operation is applied to all prime numbers less than or equal to a given number N. The function should take two parameters: `n` (the given number N) and `MOD` (a large prime number for modulo operation to avoid overflow). The function should return the result of the product modulo MOD. The time complexity of the solution should be better than O(N log N).
"""

def product_of_factorials(n, MOD):
    """
    This function calculates the product of the results when a factorial operation 
    is applied to all prime numbers less than or equal to a given number N.
    
    Parameters:
    n (int): The given number N.
    MOD (int): A large prime number for modulo operation to avoid overflow.
    
    Returns:
    int: The result of the product modulo MOD.
    """
    def generate_primes(n):
        """
        Helper function to generate all prime numbers up to N using the Sieve of Eratosthenes algorithm.
        
        Parameters:
        n (int): The upper limit for generating prime numbers.
        
        Returns:
        list: A list of all prime numbers up to N.
        """
        sieve = [True] * (n+1)
        p = 2
        while p * p <= n:
            if sieve[p] is True:
                for i in range(p*p, n + 1, p):
                    sieve[i] = False
            p += 1
        primes = [p for p in range(2, n + 1) if sieve[p]]
        return primes

    primes = generate_primes(n)
    
    product = 1
    included = [False] * (n + 1)
    for p in primes:
        for i in range(p, n + 1, p):
            included[i] = True

    for i in range(2, n+1):
        if included[i]:
            product = (product * i) % MOD
    return product