"""
QUESTION:
Implement a function named `multiplication_table` that takes an integer `n` as input and returns a 2D list representing the multiplication table up to `n` rows and 12 columns. Each row should contain the multiples of the corresponding row number from 1 to 12.
"""

def multiplication_table(n):
    table = []
    for i in range(1, 13):
        row = []
        for j in range(1, n+1):
            row.append(i * j)
        table.append(row)
    return table