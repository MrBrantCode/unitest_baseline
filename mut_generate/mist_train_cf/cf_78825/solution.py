"""
QUESTION:
Write a function `solve(data)` that takes a two-dimensional array `data` as input, calculates the sum of all individual elements (`aggregate`), and computes the sum of the diagonal elements (`diagonal_sum`). The input array is a square matrix (i.e., the number of rows equals the number of columns). Return both `aggregate` and `diagonal_sum` as output.
"""

def solve(data):
    aggregate = 0
    diagonal_sum = 0

    for i in range(len(data)):
        aggregate += sum(data[i])
        diagonal_sum += data[i][i]

    return aggregate, diagonal_sum