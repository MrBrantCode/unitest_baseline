"""
QUESTION:
Create a function `substitute_entity(matrix, old_entity, new_entity)` that substitutes the first occurrence of `old_entity` with `new_entity` in a 2D matrix containing strings and integers. The function should return a tuple of the row and column where the substitution occurred. If `old_entity` does not exist in the matrix, it should return an error message. The function should be optimized for performance, especially for large matrices.
"""

def substitute_entity(matrix, old_entity, new_entity):
    try:
        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == old_entity:
                    matrix[i][j] = new_entity
                    return(i, j)
        return 'Entity not found in matrix'
    except Exception as e:
        return str(e)