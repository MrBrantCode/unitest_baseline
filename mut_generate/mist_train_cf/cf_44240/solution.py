"""
QUESTION:
Implement the `sort_matrix` function to sort a 2D matrix in ascending order, where entire rows and columns are sorted together in ascending order. The input matrix is a list of lists of integers, and the output should be a new sorted 2D matrix. The function should handle rectangular matrices of any dimensions. 

The input matrix can contain duplicate values and may not be square. The function should not modify the original matrix. Analyze the time and space complexity of the solution and describe how to handle possible edge cases, such as non-rectangular matrices or non-2D inputs.
"""

def sort_matrix(matrix):
  # Get matrix dimensions
  rows = len(matrix)
  cols = len(matrix[0])

  # Flatten matrix into 1D list
  flatten = sum(matrix, [])

  # Sort the list in ascending order
  flatten.sort()

  # Create a copy of the matrix to avoid modifying the original
  sorted_matrix = [row[:] for row in matrix]

  # Reconstruct the sorted 2D matrix
  for i in range(rows):
    for j in range(cols):
      sorted_matrix[i][j] = flatten[i*cols+j]

  return sorted_matrix