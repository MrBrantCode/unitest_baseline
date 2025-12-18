"""
QUESTION:
Write a function `calc_matrix_product` that takes a bi-dimensional matrix as input and returns the product of all elements within the matrix. The input matrix is a list of lists where each inner list represents a row in the matrix. The function should multiply all elements in the matrix together and return the result.
"""

def calc_matrix_product(matrix):
  product = 1
  for row in matrix:
    for element in row:
      product *= element
  return product