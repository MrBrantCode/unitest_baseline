"""
QUESTION:
Write a function `multiplication_table(n)` that takes an integer `n` as input and returns a list of lists representing the multiplication table for numbers from 1 to `n`. Each inner list should represent a row in the multiplication table.
"""

def entance(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i * j)
        table.append(row)
    return table