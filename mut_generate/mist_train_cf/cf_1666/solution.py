"""
QUESTION:
Write a function `top_k_rows(matrix, k)` that takes a matrix of numbers and an integer `k` as input and returns a list of the top `k` rows with the highest sum of absolute differences between consecutive elements, excluding `None` values and in ascending order of the sum of absolute differences. The function should handle negative numbers, have a time complexity of O(nlogn), and minimize unnecessary memory usage.
"""

def top_k_rows(matrix, k):
    # Calculate the sum of absolute differences for each row
    diffs = []
    for row in matrix:
        row_diff = 0
        for i in range(len(row) - 1):
            if row[i] is not None and row[i + 1] is not None:
                row_diff += abs(row[i] - row[i + 1])
        diffs.append(row_diff)
    
    # Sort the rows based on the sum of absolute differences
    sorted_rows = [row for _, row in sorted(zip(diffs, matrix))]
    
    # Return the top k rows
    return sorted_rows[:k]