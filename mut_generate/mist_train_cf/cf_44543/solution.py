"""
QUESTION:
Create a function named `create_prime_matrix` that generates an NxN matrix where each cell at position (i, j) contains a Boolean value indicating whether the product of (i+j+2) is a prime number or not. The function should take an integer N as input and return the matrix. Additionally, print the first 10 prime numbers found in the matrix. The solution should be efficient to handle large values of N.
"""

def create_prime_matrix(n):
    """
    This function generates an NxN matrix where each cell at position (i, j) contains a Boolean value 
    indicating whether the product of (i+j+2) is a prime number or not.

    Args:
        n (int): The size of the matrix.

    Returns:
        list: A 2D list representing the matrix.
    """

    # Calculate the maximum possible value of i+j+2 in the matrix
    max_val = 2 * n + 2
    
    # Use the Sieve of Eratosthenes algorithm to find all the prime numbers up to max_val
    primes = [True for _ in range(max_val + 1)]
    p = 2
    while p * p <= max_val:
        if primes[p] == True:
            for i in range(p * p, max_val + 1, p):
                primes[i] = False
        p += 1
    
    # Create the matrix with boolean values indicating whether the product a cell's (i, j) index is prime
    prime_matrix = [[primes[i + j + 2] for j in range(n)] for i in range(n)]
    
    # Print the first 10 prime numbers that exist in the matrix
    primes_found = 0
    for row in prime_matrix:
        for cell in row:
            if primes_found >= 10:
                break
            if cell is True:
                primes_found += 1
                print(f"Prime number {primes_found}: {primes_found}")  # Changed print statement
    
    return prime_matrix