"""
QUESTION:
Write a function called `top_10_rows(matrix)` that takes a matrix as input and returns the top 10 rows with the highest sum of elements. In case of ties, rows should be sorted based on the number of negative values in ascending order. The function should only use core Python functionality and not rely on external libraries. The input matrix can be large (n > 1000, m > 1000) and may contain negative values.
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