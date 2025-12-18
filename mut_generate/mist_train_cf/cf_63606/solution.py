"""
QUESTION:
Generate a function named `generate_matrix` that creates a 2D matrix with integers. The matrix must have exactly 4 rows and 50 columns. The elements in each column of the matrix should be prime numbers.
"""

import numpy as np

def check_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def generate_matrix():
    rows = 4
    cols = 50
    prime_nums = []
    i = 2
    while len(prime_nums) < rows*cols:
        if check_prime(i):
            prime_nums.append(i)
        i += 1
    matrix = np.array(prime_nums).reshape(rows, cols)
    return matrix