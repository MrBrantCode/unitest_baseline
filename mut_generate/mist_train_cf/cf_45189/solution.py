"""
QUESTION:
Create a function called `build_matrix` that takes an integer `limit` as input and returns a matrix where each row represents the prime factors of a number from 2 to `limit`. If a number is prime, its row should contain only itself. The function should be efficient and follow number theory principles for factorization.
"""

def build_matrix(limit):
    """
    This function creates a matrix where each row represents the prime factors of a number from 2 to 'limit'.
    If a number is prime, its row contains only itself.
    
    Parameters:
    limit (int): The upper limit for generating the matrix.
    
    Returns:
    list: A 2D list where each sublist contains the prime factors of a number from 2 to 'limit'.
    """
    
    # defining a helper function to check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # defining a helper function to get the prime factors of a number
    def prime_factors(n):
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors

    # construct the matrix
    matrix = []
    for i in range(2, limit + 1):
        if is_prime(i):
            matrix.append([i])
        else:
            matrix.append(prime_factors(i))
    return matrix