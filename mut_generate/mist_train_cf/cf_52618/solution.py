"""
QUESTION:
Construct a 3D array, `tables_3d`, containing addition and multiplication tables for Fibonacci numbers generated between 0 and 10,000. The Fibonacci sequence should be generated using a memoization approach. The array should support negative indices and wrap-around. Define a function `fibonacci(n)` to generate the Fibonacci sequence and create the 3D array using the generated sequence. Ensure the array handles large numbers and is displayed in a readable format.
"""

import numpy as np

def fibonacci(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]

def generate_3d_tables():
    fibo_numbers = [fibonacci(i) for i in range(21) if fibonacci(i) <= 10000]
    size = len(fibo_numbers)
    addition_table = np.zeros((size, size), dtype=int)
    multiplication_table = np.zeros((size, size), dtype=int)

    for i in range(size):
        for j in range(size):
            addition_table[i, j] = fibo_numbers[i] + fibo_numbers[j]
            multiplication_table[i, j] = fibo_numbers[i] * fibo_numbers[j]

    tables_3d = np.dstack([addition_table, multiplication_table])
    return tables_3d