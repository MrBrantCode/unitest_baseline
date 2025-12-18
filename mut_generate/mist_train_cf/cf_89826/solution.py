"""
QUESTION:
Write a function named `top_10_rows` that takes a 2D list (or matrix) of integers as input, where the matrix size is n x m and n and m are large integers. The function should return the top 10 rows from the matrix based on the following criteria: 

- The rows are first sorted in descending order based on the sum of their elements.
- If there are ties in the sums, the rows are then sorted in ascending order based on the number of negative values in each row.

The function should use only core Python functionality and have a time complexity of O(nlogn) or better.
"""

def top_10_rows(matrix):
    rows = []
    for row in matrix:
        row_sum = sum(row)
        num_negatives = sum(1 for num in row if num < 0)
        rows.append((row_sum, num_negatives, row))
    
    rows.sort(key=lambda x: (-x[0], x[1]))
    
    return rows[:10]