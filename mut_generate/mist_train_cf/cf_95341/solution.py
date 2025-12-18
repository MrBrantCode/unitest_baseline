"""
QUESTION:
Create a function named `create_matrix` that takes an integer `n` as input and returns an `n x n` matrix filled with 0s, where `n` is a prime number. The function should fill the diagonal of the matrix with 1s. If `n` is not a prime number, the function should return `None`.
"""

def create_matrix(n):
    # Check if n is a prime number
    if not is_prime(n):
        return None
    
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    
    return matrix

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True