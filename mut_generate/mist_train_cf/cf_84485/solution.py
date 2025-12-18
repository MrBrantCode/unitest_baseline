"""
QUESTION:
Create a function called `fibonacci` that generates Fibonacci numbers within a given range (0 to 1000) and arranges them in a square matrix (a 2D list) of minimum size, padding with None values as necessary. The Fibonacci numbers should be filled in the matrix in row-major order.
"""

import numpy as np

def fibonacci(n):
    fib_nums = [0, 1]
    while fib_nums[-1] + fib_nums[-2] <= n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    
    matrix_size = int(np.ceil(np.sqrt(len(fib_nums))))
    fib_matrix = [[None]*matrix_size for _ in range(matrix_size)]
    
    for index, num in enumerate(fib_nums):
        fib_matrix[index//matrix_size][index%matrix_size] = num
        
    return fib_matrix