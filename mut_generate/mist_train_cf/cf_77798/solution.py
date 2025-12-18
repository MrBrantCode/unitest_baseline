"""
QUESTION:
Write a function `matrix_prime_sum(matrix)` that calculates the sum of prime numbers in a given 2D matrix. A prime number is considered for the sum if it has at least one prime number in any of its eight neighboring positions (left, right, up, down, or diagonals). The function should be optimized for large matrices. Assume that the input matrix is a 2D array of integers and its rows and columns are greater than 1.
"""

import numpy as np

def check_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

def get_prime_neighbors(i, j, matrix):
    rows, cols = matrix.shape
    prime_numbers = []
    for in_i in range(max(0, i-1), min(rows, i+2)):
        for in_j in range(max(0, j-1), min(cols, j+2)):
            if in_i != i or in_j != j:
                if check_prime(matrix[in_i][in_j]):
                    prime_numbers.append(matrix[in_i][in_j])
    return prime_numbers

def matrix_prime_sum(matrix):
    rows, cols = matrix.shape
    prime_sum = 0
    for i in range(rows):
        for j in range(cols):
            if check_prime(matrix[i][j]):
                prime_neighbors = get_prime_neighbors(i, j, matrix)
                if len(prime_neighbors) > 0:
                    prime_sum += matrix[i][j]
    return prime_sum