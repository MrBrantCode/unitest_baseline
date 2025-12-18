"""
QUESTION:
Create a function `transform_matrix(mat)` that takes a 2D matrix of integers as input and returns a 1D list. The function should first flatten the matrix into a list, then rearrange the list such that all prime numbers appear before non-prime numbers while maintaining their relative order from the original matrix. The function should handle negative numbers and zero, and should not use built-in prime number checking methods.
"""

def transform_matrix(mat):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        m = int(n ** 0.5) + 1
        for x in range(3, m, 2):
            if n % x == 0:
                return False
        return True

    flattened = [item for sublist in mat for item in sublist]
    primes = list(filter(is_prime, flattened))
    not_primes = list(filter(lambda x: not is_prime(x), flattened))
    return primes + not_primes