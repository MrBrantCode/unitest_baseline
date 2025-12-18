"""
QUESTION:
Create a function `add_matrices_with_primes(matrix1, matrix2)` that takes two square matrices as input. `matrix1` is any square matrix, and `matrix2` is an identity matrix of the same size. The function must only accept matrices with dimensions between 2 and 10 (inclusive). It should return the result of adding the two matrices together, but only if all elements in the resulting matrix are prime numbers; otherwise, return `None`.
"""

def add_matrices_with_primes(matrix1, matrix2):
    # Check if matrix dimensions are valid
    size = len(matrix1)
    if size != len(matrix2) or size < 2 or size > 10:
        return None

    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Create the result matrix
    result = [[0] * size for _ in range(size)]

    # Iterate over each element and add them together
    for i in range(size):
        for j in range(size):
            result[i][j] = matrix1[i][j] + matrix2[i][j]

    # Check if each element is a prime number
    for i in range(size):
        for j in range(size):
            if not is_prime(result[i][j]):
                return None

    return result