"""
QUESTION:
Create a recursive function named "complex_matrix_multiply" that takes two matrices with complex numbers as input and returns their product. The function should check if the input matrices have compatible dimensions for multiplication (i.e., the number of columns in the first matrix equals the number of rows in the second matrix). If they are not compatible, the function should return an error message. The matrix multiplication should be performed using only the real and imaginary parts of the complex numbers, without using any built-in complex number multiplication functions.
"""

def complex_matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return "Error: Incompatible dimensions for matrix multiplication"

    result = [[0+0j] * len(matrix2[0]) for _ in range(len(matrix1))]

    def multiply_recursive(matrix1, matrix2, result, row1, col2, col1):
        if col2 == len(matrix2[0]):
            row1 += 1
            col2 = 0
        if row1 == len(matrix1):
            return result

        sum_real = 0
        sum_imaginary = 0

        for i in range(len(matrix1[0])):
            a = matrix1[row1][i]
            b = matrix2[i][col2]

            sum_real += a.real * b.real - a.imag * b.imag
            sum_imaginary += a.real * b.imag + a.imag * b.real

        result[row1][col2] = (sum_real + sum_imaginary * 1j)
        
        multiply_recursive(matrix1, matrix2, result, row1, col2+1, col1)
        multiply_recursive(matrix1, matrix2, result, row1+1, col2, col1)
    
    multiply_recursive(matrix1, matrix2, result, 0, 0, 0)
    return result