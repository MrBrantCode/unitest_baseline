"""
QUESTION:
Write a function called `prime_product` that takes an integer `n` as input and returns the product of all prime numbers less than or equal to `n`, along with the list of identified prime numbers and the count of primes. The function should use the Sieve of Eratosthenes algorithm to identify prime numbers. If the input `n` is not an integer or is less than 2, the function should handle the error and return an appropriate message.
"""

def prime_product(n):
    """
    This function takes an integer n as input and returns the product of all prime numbers less than or equal to n,
    along with the list of identified prime numbers and the count of primes.
    
    Args:
        n (int): The input integer.

    Returns:
        tuple: A tuple containing the product of prime numbers, list of prime numbers, and the count of primes.
    """

    # Check the type of n and if it is less than 2
    if not isinstance(n, int) or n < 2:
        return "Invalid input. Please enter an integer greater than 1."

    # Create a boolean array "primes[0..n]" and initialize all entries it as true.
    # A value in primes[i] will finally be false if i is Not a prime, else true.
    primes = [True for i in range(n+1)]
    p = 2

    # Iterate over the array and mark the multiples of each prime number starting from 2
    while (p * p <= n): 
        # If primes[p] is not changed, then it is a prime
        if (primes[p] == True): 
            # Update all multiples of p
            for i in range(p * p, n+1, p): 
                primes[i] = False
        p += 1
    
    # Collect all prime numbers
    prime_nums = [p for p in range(2, n+1) if primes[p]]

    # Calculate the product of prime numbers
    product = 1
    for prime in prime_nums:
        product *= prime

    return product, prime_nums, len(prime_nums)