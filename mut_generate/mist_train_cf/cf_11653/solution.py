"""
QUESTION:
Create a function `create_matrix(N)` that takes an integer `N` as input and returns an NxN matrix with all elements initialized to 0, but only if `N` is a prime number. If `N` is not a prime number, the function should return `None`.
"""

def create_matrix(N):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    if not is_prime(N):
        return None
    
    matrix = [[0] * N for _ in range(N)]
    return matrix