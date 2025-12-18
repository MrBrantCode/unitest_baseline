"""
QUESTION:
Create a function `has_symmetrical_rows(matrix)` that determines if a given matrix has any symmetrical row pairs. The function should return `True` along with the pair of row indices if a symmetrical pair is found; otherwise, it should return `False` along with an empty tuple. The input matrix is a list of lists or a list of tuples, where each inner list or tuple represents a row in the matrix. The function should not modify the original matrix.
"""

def has_symmetrical_rows(matrix):
    
    # Empty dictionary to store seen rows
    seen = {}
    
    # Iterate over rows in matrix
    for i, row in enumerate(matrix):

        # Convert each row to tuple so it can be added to a dictionary
        row_tuple = tuple(row)

        # If reversed row already seen
        if row_tuple[::-1] in seen:
            
            # Return True and the pair
            return True, (seen[row_tuple[::-1]], i)

        # Otherwise add row to seen dict
        seen[row_tuple] = i
    
    # If no symmetry found
    return False, ()