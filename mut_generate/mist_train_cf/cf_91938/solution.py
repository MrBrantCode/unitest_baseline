"""
QUESTION:
Create a function named `create_matrix` that takes an integer `N` as input, where `N` must be a prime number. The function should return a 2D list (or matrix) of size NxN with all elements initialized to 0. If `N` is not a prime number, the function should print an error message and return `None`.
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
        print("N must be a prime number.")
        return None
    
    matrix = [[0] * N for _ in range(N)]
    return matrix