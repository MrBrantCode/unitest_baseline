"""
QUESTION:
Write a function named `row_sums` that takes a matrix of positive integers (where each integer does not exceed 1000) as input and returns a vector of length M+1, where M is the number of rows in the matrix. The first M elements of the vector should contain the sum of each row in the matrix, and the last element should be the sum of all elements in the matrix.
"""

def row_sums(matrix):
    # Initialize the vector with all zeros
    result = [0] * (len(matrix) + 1)

    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Calculate the sum of the current row
        row_sum = sum(matrix[i])
        # Add the row sum to the vector
        result[i] = row_sum
        # Add the row sum to the total sum
        result[-1] += row_sum

    return result