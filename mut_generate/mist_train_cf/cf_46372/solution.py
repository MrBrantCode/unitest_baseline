"""
QUESTION:
Create a function named `primes_in_matrix` that takes a 2D matrix of integers as input. The function should return a copy of the original matrix but with all prime numbers replaced with 1 and all non-prime numbers replaced with 0. The input matrix can be up to 100x100 in size.
"""

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def primes_in_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if is_prime(matrix[i][j]):
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
    return matrix