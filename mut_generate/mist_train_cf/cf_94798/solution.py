"""
QUESTION:
Given a matrix of size n x m containing integers in the range -10^9 to 10^9, write a function `calculate_sum(matrix)` to calculate the sum of all positive elements excluding the minimum positive element in each row. The matrix can have rows and columns of different lengths, up to 10^5 rows and 10^5 columns, and may contain duplicate values.
"""

def calculate_sum(matrix):
    total_sum = 0
    min_positives = set()

    for row in matrix:
        row_min = float('inf')
        for element in row:
            if element > 0:
                total_sum += element
                row_min = min(row_min, element)
        if row_min != float('inf'):
            min_positives.add(row_min)

    for min_positive in min_positives:
        total_sum -= min_positive

    return total_sum