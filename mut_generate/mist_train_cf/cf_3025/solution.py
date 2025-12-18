"""
QUESTION:
Write a function named `sum_of_prime_factors` that takes an integer `N` as input, finds all prime factors of `N` (greater than 1), adds them together, and returns the result. The function must be implemented recursively, not use any built-in mathematical or prime factorization functions or libraries, and only accept positive integers greater than 1.
"""

def sum_of_prime_factors(N, divisor=2, prime_factors=set()):
    # Base case: N is 1, return the sum of prime factors
    if N == 1:
        return sum(prime_factors)
    
    # Check if divisor is a prime factor of N
    if N % divisor == 0:
        prime_factors.add(divisor)
        return sum_of_prime_factors(N // divisor, divisor, prime_factors)
    
    # Increment the divisor and call the function recursively
    return sum_of_prime_factors(N, divisor + 1, prime_factors)