"""
QUESTION:
Write a function `top_10_rows(matrix)` that takes a 2D list `matrix` of integers as input and returns the top 10 rows based on the following criteria: 
- The sum of elements in each row in descending order.
- In case of ties in the sums, the rows are sorted based on the number of negative values in each row in ascending order.
- The function should only use core Python functionality and should have a time complexity of O(nlogn) or better.
"""

def top_10_rows(matrix):
    rows = []
    for row in matrix:
        row_sum = sum(row)
        num_negatives = sum(1 for num in row if num < 0)
        rows.append((row_sum, num_negatives, row))
    
    rows.sort(key=lambda x: (-x[0], x[1]))
    
    return rows[:10]