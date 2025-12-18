"""
QUESTION:
Implement a function called `multiplication_table` that takes an integer `n` and returns a 2D list representing the multiplication table of numbers from 1 to `n` up to 12. The function should return a list of lists where each inner list represents a row in the multiplication table. Each inner list should contain 12 elements, representing the product of the row number and the numbers from 1 to 12.
"""

def multiplication_table(n):
    table = []
    for i in range(1, 13):
        row = []
        for j in range(1, n+1):
            row.append(i * j)
        table.append(row)
    return table