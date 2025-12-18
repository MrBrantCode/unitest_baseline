"""
QUESTION:
Write a function named `column_sums` that takes a 2D array as input and returns a 1D array containing the sum of each column. The function should assume that the input array is not empty and all rows have the same number of columns.
"""

def column_sums(arr):
  # Calculate the number of rows and columns in the array
  n = len(arr)
  m = len(arr[0])

  # Create a new array of size m to store the sums
  sums = [0] * m

  # Calculate the sum of each column
  for j in range(m):
    column_sum = 0
    for i in range(n):
      column_sum += arr[i][j]
    sums[j] = column_sum

  return sums