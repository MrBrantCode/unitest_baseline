"""
QUESTION:
Create a function `arrange_matrix` that takes a square matrix of integers as input and returns a rearranged matrix where no two identical elements share the same row or column. If no such arrangement is possible, return the string "Matrix can't be arranged". The input matrix contains only integers and has an equal number of rows and columns.
"""

def arrange_matrix(matrix):
    def solve(matrix, i, used):
        if i == len(matrix):
            return True

        for j in range(len(matrix)):
            if all(matrix[i][j] != matrix[k][j] for k in range(i)) and j not in used:
                used.add(j)
                if solve(matrix, i+1, used):
                    return True
                used.remove(j)

        return False

    sorted_matrix = sorted((v, i) for i, row in enumerate(matrix) for v in sorted(row))
    sorted_matrix = [ sorted_matrix[i:i+len(matrix)] for i in range(0, len(sorted_matrix), len(matrix)) ]
    sorted_matrix = [ [cell[0] for cell in row] for row in sorted_matrix ]

    for v, i in sorted(sorted((row[0], i) for i, row in enumerate(sorted_matrix))):
        sorted_matrix[i] = [v] + sorted_matrix[i][1:]

    can_be_arranged = solve(sorted_matrix, 0, set())
        
    return sorted_matrix if can_be_arranged else "Matrix can't be arranged"