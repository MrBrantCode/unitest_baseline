"""
QUESTION:
Write a function `sum_of_diagonals(matrix)` that takes a 3D matrix as input and returns the sum of its diagonals from top-left to bottom-right. The function should be efficient, with a complexity of O(n), where n is the total number of elements in the matrix. The matrix can contain negative numbers.
"""

def sum_of_diagonals(matrix):
    f = len(matrix)
    g = len(matrix[0])
    h = len(matrix[0][0])
    diag_dict = {}
    for z in range(f):
        for y in range(g):
            for x in range(h):
                if z + y + x not in diag_dict:
                    diag_dict[z+y+x] = []
                diag_dict[z + y + x].append(matrix[z][y][x])
    return sum(sum(diag_dict[i]) for i in diag_dict.keys())