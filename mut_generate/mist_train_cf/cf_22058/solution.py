"""
QUESTION:
Create a function `generate_multiplication_table(N)` that generates a 2D list containing a multiplication table up to a given number N. The function should only use basic arithmetic operations and not rely on any built-in functions or libraries. The function should be able to handle large values of N efficiently.
"""

def generate_multiplication_table(N):
    table = []
    for i in range(1, N+1):
        row = []
        for j in range(1, N+1):
            row.append(i * j)
        table.append(row)
    return table