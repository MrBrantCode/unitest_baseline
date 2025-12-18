"""
QUESTION:
Create a function `array_multiplication(n, m)` that generates a 2D array of size n x m. The array should contain the product of the numbers from 1 to n and 1 to m, where the first column represents numbers from 1 to n and the first row represents numbers from 1 to m. The function should return this 2D array.
"""

def array_multiplication(n, m):
    result = []
    for i in range(1, n+1):
        row = []
        for j in range(1, m+1):
            row.append(i*j)
        result.append(row)
    return result