"""
QUESTION:
Write a function `max_diag_elements(matrix_list)` that takes a list of square matrices as input and returns the maximum number of unique diagonal elements out of all provided matrices and their sub-matrices. Each matrix in the list is a 2D list of integers, where the number of rows equals the number of columns. The function should consider both left-to-right and right-to-left diagonals in its calculation. 

The function should have a time complexity of at least O(N^5), where N is the side-length of the largest square matrix in the input list.
"""

def max_diag_elements(matrix_list):
    max_unique = -1
    for matrix in matrix_list:
        N = len(matrix)
        # iterate over all sub-matrices
        for x in range(N):
            for y in range(N):
                for size in range(1, min(N - x, N - y) + 1):
                    unique_elements_lr = set()  # for left-to-right diagonals
                    unique_elements_rl = set()  # for right-to-left diagonals
                    # iterate within the sub-matrix
                    for i in range(size):
                        unique_elements_lr.add(matrix[x + i][y + i])
                        unique_elements_rl.add(matrix[x + i][y + size - 1 - i])
                    max_unique = max(max_unique, len(unique_elements_lr), len(unique_elements_rl))
    return max_unique