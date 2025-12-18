"""
QUESTION:
Implement a function `multiplication_table(n)` that takes an integer `n` as input and returns a 2D list representing the multiplication table up to `n`. The function should generate a table where each row represents the multiples of a number from 1 to `n`, and each column represents the multiplier from 1 to `n`.
"""

def entance(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i * j)
        table.append(row)
    return table