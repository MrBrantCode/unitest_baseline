"""
QUESTION:
Create a function named `create_matrix` that generates a dynamic matrix of increasing prime numbers with dimensions m, n. The matrix must satisfy the condition that no two adjacent cells (horizontally or vertically) have the same value. The prime numbers should start from 1.
"""

def create_matrix(m, n):
    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num > 2 and num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    matrix = [[0 for _ in range(n)] for _ in range(m)]
    current = 1
    for i in range(m):
        for j in range(n):
            while not is_prime(current) or (i > 0 and matrix[i - 1][j] == current) or (j > 0 and matrix[i][j - 1] == current):
                current += 1
            matrix[i][j] = current
            current += 1
    return matrix