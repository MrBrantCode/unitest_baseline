"""
QUESTION:
Design a function `arrange_matrix` that takes a matrix as input and returns a dictionary containing the index of the row that needs rearranging to sort the matrix column-wise, the index of the row with which it should be swapped, and the total number of rearrangements needed. If the matrix is already sorted or no such row exists, return {'row_index': -1, 'rearrange_with': -1, 'total_rearrangements': 0}. The input matrix has no duplicate rows.
"""

def arrange_matrix(mat):
    """
    This function analyzes a given matrix to identify unsorted rows and 
    find potential rearrangement possibilities to sort the matrix column-wise.
    
    Args:
    mat (list): A 2D list representing the input matrix.

    Returns:
    dict: A dictionary containing the index of the row that needs rearranging, 
    the index of the row with which it should be swapped, and the total number of rearrangements needed.
    If the matrix is already sorted or no such row exists, return {'row_index': -1, 'rearrange_with': -1, 'total_rearrangements': 0}.
    """
    
    def is_sorted(matrix):
        """Check if the matrix is sorted column-wise."""
        for col_idx in range(len(matrix[0])):
            column = [row[col_idx] for row in matrix]
            if column != sorted(column):
                return False
        return True

    # Initialize variables to store the result
    result = {'row_index': -1, 'rearrange_with': -1, 'total_rearrangements': 0}
    rearrangements = 0
    
    # Iterate over each row in the matrix
    for i in range(len(mat)):
        # Check if the matrix is sorted after each iteration
        if is_sorted(mat):
            break
        
        # Check if the current row needs to be rearranged
        for j in range(i + 1, len(mat)):
            # Create a copy of the matrix to test the swap
            swapped_mat = [row[:] for row in mat]
            swapped_mat[i], swapped_mat[j] = swapped_mat[j], swapped_mat[i]
            
            # Check if the swapped matrix is sorted
            if is_sorted(swapped_mat):
                # Update the result and increment the rearrangement count
                result['row_index'] = i
                result['rearrange_with'] = j
                rearrangements += 1
                
                # Swap the rows in the original matrix
                mat[i], mat[j] = mat[j], mat[i]
                break
    
    # Update the total rearrangements in the result
    result['total_rearrangements'] = rearrangements
    
    return result