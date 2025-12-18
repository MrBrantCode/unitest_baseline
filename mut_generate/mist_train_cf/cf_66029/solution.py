"""
QUESTION:
Develop a recursive function `primes_in_range(C, D)` that prints all prime numbers within the inclusive range [C, D]. The function should use an additional helper function `is_prime(N)` to check if a number is prime. The function should be able to handle any range [C, D] but may not be suitable for large ranges due to potential maximum recursion depth errors.
"""

def primes_in_range(C, D):
    """
    Prints all prime numbers within the inclusive range [C, D].
    
    Args:
        C (int): The start of the range (inclusive).
        D (int): The end of the range (inclusive).
    """
    if C > D:
        return
    if C == 1:
        primes_in_range(C+1, D)
    elif C == 2: 
        print(C)
        primes_in_range(C+1, D)
    else:
        if is_prime(C):
            print(C)
        primes_in_range(C+1, D)


def is_prime(N, i=2):
    """
    Checks if a number is prime.
    
    Args:
        N (int): The number to check.
        i (int): The current divisor to check (default is 2).
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if N <= 2:
        if N == 2:
            return True
        return False
    if N % i == 0:
        return False
    if i * i > N:
        return True
    
    return is_prime(N, i+1)