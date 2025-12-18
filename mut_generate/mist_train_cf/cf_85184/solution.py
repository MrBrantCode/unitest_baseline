"""
QUESTION:
Write a function `spiral_4d` that prints a 4D matrix in a spiral order. The function should take a 4D matrix (n x m x p x q) as input, where n, m, p, q > 0. The function should handle variable array dimensions and be robust against potential variations in the length of subarrays. If the input is invalid, the function should return a descriptive error message.
"""

def spiral_4d(matrix):
    def spiral_print(mat):
        while mat:
            for line in mat.pop(0): 
                print(line, end=' ')
            for v in mat: 
                print(v.pop(), end=' ')
            if mat and mat[0]: 
                for line in mat.pop()[::-1]: 
                    print(line, end=' ')
            for v in mat[::-1]:
                print(v.pop(0), end=' ')

    if not all(isinstance(sub, list) for sub in matrix):
        return 'Invalid matrix.'
    try:
        for cube in matrix:
            for mat in cube:
                spiral_print(mat)
    except (TypeError, IndexError):
        return 'Invalid matrix.'
    return 