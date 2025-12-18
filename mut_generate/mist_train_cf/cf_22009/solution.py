"""
QUESTION:
Write a function called `convert_to_1D` that takes a 2D matrix as input. The function should return a 1D array if the input is a valid 2D matrix, where each row has the same number of elements, and all elements are integers between -100 and 100 inclusive. If the input matrix is not valid, the function should return an error message "Invalid matrix. Rows have different lengths."
"""

def convert_to_1D(matrix):
    """
    This function takes a 2D matrix as input and returns a 1D array.
    If the input matrix is not valid, it returns an error message.
    
    A valid matrix is defined as a 2D list where each row has the same number of elements,
    and all elements are integers between -100 and 100 inclusive.
    
    Parameters:
    matrix (list): A 2D list of integers.
    
    Returns:
    list: A 1D list of integers or an error message if the input matrix is not valid.
    """
    
    # Check if the matrix is a valid 2D matrix
    if not matrix:  # Check if the matrix is empty
        return "Invalid matrix. Matrix is empty."
    
    row_length = len(matrix[0])
    for i, row in enumerate(matrix):
        # Check if the row has the same number of elements as the first row
        if len(row) != row_length:
            return "Invalid matrix. Rows have different lengths."
        
        # Check if all elements are integers between -100 and 100 inclusive
        for j, num in enumerate(row):
            if not isinstance(num, int) or num < -100 or num > 100:
                return f"Invalid matrix. Element at row {i+1}, column {j+1} is out of range."
    
    # Convert the matrix into a 1D array
    array = []
    for row in matrix:
        array.extend(row)
    
    return array