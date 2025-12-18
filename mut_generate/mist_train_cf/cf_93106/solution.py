"""
QUESTION:
Create a function called `generate_multiplication_table` that takes an integer `N` as input and returns a 2D list containing the multiplication table up to `N`. The function should be able to handle large values of `N` efficiently.
"""

def generate_multiplication_table(N):
    table = []
    for i in range(1, N+1):
        row = [i*j for j in range(1, N+1)]
        table.append(row)
    return table