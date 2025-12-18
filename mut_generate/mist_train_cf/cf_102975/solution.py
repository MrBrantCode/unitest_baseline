"""
QUESTION:
Create a function named `calculate_dot_product` that calculates the dot product of a given 4x4 matrix and a 4x1 matrix. The matrices can only contain integers ranging from -10 to 10. The function should use the formula for dot product calculation, which involves summing the products of corresponding elements from each matrix.
"""

def calculate_dot_product(matrix1, matrix2):
    """
    This function calculates the dot product of a given 4x4 matrix and a 4x1 matrix.
    
    Args:
        matrix1 (list): A 4x4 matrix containing integers ranging from -10 to 10.
        matrix2 (list): A 4x1 matrix containing integers ranging from -10 to 10.
    
    Returns:
        int: The dot product of the two matrices.
    """
    
    # Initialize the dot product
    dot_product = 0
    
    # Iterate over each row in matrix1 and the corresponding element in matrix2
    for i in range(len(matrix1)):
        # Multiply the corresponding elements and add to the dot product
        dot_product += sum(a * b for a, b in zip(matrix1[i], [matrix2[i]] * len(matrix1[i])))
    
    # Return the calculated dot product
    return dot_product