"""
QUESTION:
Create a function `generate_multiplication_table` that takes an integer `N` as input and returns a 2D list representing the multiplication table up to `N`. The function should only use basic arithmetic operations and should be able to handle large values of `N` efficiently.
"""

def generate_multiplication_table(N):
    table = []
    for i in range(1, N+1):
        row = []
        for j in range(1, N+1):
            row.append(i * j)
        table.append(row)
    return table