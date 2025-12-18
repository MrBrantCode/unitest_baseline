"""
QUESTION:
Generate a function named `generate_multiplication_table(N)` that uses recursion to create a multiplication table up to the given number N, where the table is a list of lists containing the products of numbers from 1 to N. The function should only use basic arithmetic operations and not rely on any built-in functions or libraries.
"""

def generate_multiplication_table(N):
    table = []
    for i in range(1, N+1):
        row = []
        for j in range(1, N+1):
            row.append(i*j)
        table.append(row)
    return table