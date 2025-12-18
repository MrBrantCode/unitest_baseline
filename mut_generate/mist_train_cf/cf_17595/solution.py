"""
QUESTION:
Write a function `calculate_sum(matrix)` that takes a matrix of integers as input and returns the sum of all positive elements in the matrix, excluding any negative numbers and the minimum positive element in each row. The matrix can contain both positive and negative integers, have duplicate values, and have rows and columns of different lengths, with up to 10^5 rows and 10^5 columns, and elements ranging from -10^9 to 10^9.
"""

def calculate_sum(matrix):
    total_sum = 0
    min_positives = set()

    for row in matrix:
        row_min_positive = float('inf')
        for element in row:
            if element > 0:
                total_sum += element
                row_min_positive = min(row_min_positive, element)
        if row_min_positive != float('inf'):
            min_positives.add(row_min_positive)

    return total_sum - sum(min_positives)