"""
QUESTION:
Write a function named `processMatrix` that takes a 2D matrix as input and returns a new matrix where each element is the result of some processing operation on the corresponding element in the input matrix. The processing operation is not specified and should be left as a placeholder for now. The output matrix should have the same dimensions as the input matrix.
"""

def processMatrix(matrix):
  result_matrix = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))] 
  for row in range(len(matrix)):
    for col in range(len(matrix[0])):
      element = matrix[row][col]
      # perform processing on element here
      result_matrix[row][col] = element
  return result_matrix