"""
QUESTION:
Extract the top 10 rows from a large matrix. The function `extract_top_10_rows` takes a 2D list (matrix) as input, where the size of the matrix is n x m, and n and m are large integers. The function should return a new matrix containing the top 10 rows with the highest sum of elements in each row. The solution should only use core Python functionality.
"""

def extract_top_10_rows(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    # Create a list to store the sums of each row
    row_sums = []
    
    # Iterate over each row and calculate the sum
    for row in matrix:
        row_sums.append(sum(row))
    
    # Sort the row sums in descending order and get the indices of the top 10 rows
    top_10_indices = sorted(range(num_rows), key=lambda i: row_sums[i], reverse=True)[:10]
    
    # Create a new matrix to store the top 10 rows
    top_10_matrix = []
    
    # Iterate over the top 10 indices and extract the corresponding rows from the original matrix
    for index in top_10_indices:
        top_10_matrix.append(matrix[index])
    
    return top_10_matrix