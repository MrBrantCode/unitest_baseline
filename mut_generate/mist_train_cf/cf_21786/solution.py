"""
QUESTION:
Write a function `top_10_rows(matrix)` that takes a 2D list `matrix` of integers as input and returns the top 10 rows. The top 10 rows are determined by the sum of their elements in descending order. In case of ties, the rows are sorted by the number of negative values in each row in ascending order. The input matrix may contain negative values and has a size of n x m where n and m are large integers. The function should use only core Python functionality without relying on external libraries.
"""

def top_10_rows(matrix):
    row_stats = []
    for i, row in enumerate(matrix):
        row_sum = sum(row)
        negatives = sum(1 for element in row if element < 0)
        row_stats.append((i, row_sum, negatives))

    row_stats.sort(key=lambda x: (-x[1], x[2]))

    top_10 = row_stats[:10]
    top_10_rows = [matrix[i] for i, _, _ in top_10]

    return top_10_rows