"""
QUESTION:
Write a function `find_symmetric_pairs(matrix)` that takes a matrix as input and returns a tuple of two indices if there exists a symmetric pair of rows in the matrix. A symmetric pair of rows is a pair where one row is the reverse of the other. If no symmetric pair exists, return `None`. The matrix can be of any size, and the function should be efficient for large matrices.
"""

def find_symmetric_pairs(matrix):
    # Initialize an empty dictionary to store the rows and their reverse counterparts
    rows = {}
    
    for i in range(len(matrix)):
        # Convert each row to a tuple to make it hashable
        row = tuple(matrix[i])
        # Compute the reversed row
        reversed_row = tuple(reversed(matrix[i]))
        
        # Check if the reversed row is in the dictionary
        if reversed_row in rows:
            # If the reversed row is in the dictionary, we found a symmetric pair.
            # The symmetric pair is identified by the current row index and the stored row index.
            symmetric_pair = (rows[reversed_row], i)
            return symmetric_pair
        else:
            # If the reversed row is not in the dictionary, add the current row to the dictionary.
            rows[row] = i

    # If no symmetric pair is found, return None
    return None