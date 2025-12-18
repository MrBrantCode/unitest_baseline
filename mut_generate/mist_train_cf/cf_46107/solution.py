"""
QUESTION:
Write a function `sort_matrix` that takes a square matrix of size n x n as input and returns a new matrix where elements in each row are in increasing order and elements in each column are in decreasing order. Each element in the sorted matrix should also be in decreasing order with respect to rows and columns. The function should have an optimized time complexity. Assume that the input matrix is a square matrix of size n x n.
"""

def sort_matrix(matrix):
    # Convert the matrix to a single list
    single_list = [j for i in matrix for j in i]
    # Sort the list in decreasing order
    single_list.sort(reverse=True)
    # Convert the list back into a matrix
    sorted_matrix = [single_list[i * len(matrix):(i + 1) * len(matrix)] for i in range(len(matrix))]

    return sorted_matrix