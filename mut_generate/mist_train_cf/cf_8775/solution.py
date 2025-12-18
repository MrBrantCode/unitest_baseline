"""
QUESTION:
Create a function called `multiply_matrices(matrix1, matrix2)` that takes two matrices as input and returns their product. The number of columns in `matrix1` should be equal to the number of rows in `matrix2`. The elements in the matrices can be integers or floats, ranging from -100 to 100, and the size of the matrices can range from 1x1 to 10x10. The time complexity of the solution should be O(N^3), where N is the number of rows/columns in the matrices, and the space complexity should be O(N^2).
"""

def multiply_matrices(matrix1, matrix2):
    # Check if the number of columns in matrix1 is equal to the number of rows in matrix2
    if len(matrix1[0]) != len(matrix2):
        return "Cannot multiply matrices. The number of columns in matrix1 should be equal to the number of rows in matrix2."
    
    # Initialize an empty matrix to store the product
    product = []
    
    # Iterate over the rows of matrix1
    for i in range(len(matrix1)):
        # Initialize an empty row to store the products
        row = []
        
        # Iterate over the columns of matrix2
        for j in range(len(matrix2[0])):
            # Initialize a variable to store the product of dot products
            dot_product = 0
            
            # Perform dot product between the ith row of matrix1 and the jth column of matrix2
            for k in range(len(matrix2)):
                dot_product += matrix1[i][k] * matrix2[k][j]
            
            # Append the dot product to the row
            row.append(dot_product)
        
        # Append the row to the product matrix
        product.append(row)
    
    return product