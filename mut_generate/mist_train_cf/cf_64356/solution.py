"""
QUESTION:
Create a class `Matrix` that takes a 2D list `matrix` as input. The class should have methods to perform the following operations:
- `add(other)`: add two matrices element-wise and return the result. If the matrices are not of the same size, return an error message.
- `subtract(other)`: subtract one matrix from another element-wise and return the result. If the matrices are not of the same size, return an error message.
- `multiply(other)`: multiply two matrices and return the result. If the matrices are not compatible for multiplication, return an error message.
- `transpose()`: transpose a matrix and return the result.
 
The input matrix is a 2D list of integers, and the output of each operation should also be a 2D list of integers or an error message.
"""

def matrix_operations(matrix):
    class Matrix:
        def __init__(self, matrix):
            self.matrix = matrix

        def add(self, other):
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                return "Error: Matrices are not of the same size"
            
            result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
              
            return result

        def subtract(self, other):
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                return "Error: Matrices are not of the same size"
            
            result = [[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
            
            return result

        def multiply(self, other):
            if len(self.matrix[0]) != len(other.matrix):
                return "Error: Incompatible matrices for multiplication"
            
            result = [[sum(x * y for x, y in zip(self.matrix_row, other.matrix_col)) 
                       for other.matrix_col in zip(*other.matrix)] 
                       for self.matrix_row in self.matrix]
            
            return result

        def transpose(self):
            result = [[self.matrix[j][i] for j in range(len(self.matrix))] 
                      for i in range(len(self.matrix[0]))]
            
            return result

    return Matrix(matrix)