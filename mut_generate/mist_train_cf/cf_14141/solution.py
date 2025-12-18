"""
QUESTION:
Create a function `generate_multiplication_table(N)` that generates a list containing the multiplication table up to a given number N. The function should be able to handle large values of N efficiently, and return a list of lists where each inner list represents a row in the multiplication table, with each element being the product of the row number and column number.
"""

def generate_multiplication_table(N):
    table = []
    for i in range(1, N+1):
        row = [i*j for j in range(1, N+1)]
        table.append(row)
    return table