"""
QUESTION:
Write a function named `column_sums` that calculates the sum of each column in a given 2-dimensional array and returns a new array containing the sums. The input array is of size n x m, and the output array should be of size m.
"""

def column_sums(arr):
  n = len(arr)
  m = len(arr[0])
  sums = [0] * m
  for j in range(m):
    column_sum = 0
    for i in range(n):
      column_sum += arr[i][j]
    sums[j] = column_sum
  return sums