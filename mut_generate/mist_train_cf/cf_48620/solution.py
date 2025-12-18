"""
QUESTION:
Create a function `generate_prime_matrix(n)` that generates an n x n matrix filled with prime integers, starting from the smallest prime number (2) and continuing in ascending order. The function should not take any other parameters besides `n`, and the matrix should be filled row by row from left to right and top to bottom.
"""

import numpy as np

def generate_prime_matrix(n):
    prime_matrix = np.zeros((n, n), dtype=int)
    count = 0
    num = 2
   
    while count < (n * n):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_matrix[count // n][count % n] = num
            count += 1
        num += 1
    return prime_matrix