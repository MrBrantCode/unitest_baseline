"""
QUESTION:
Create a function `sum_of_cubes(array)` that calculates the sum of the cubes of all elements in the given array, but subtracts the cube of every third element instead of adding it. The index count starts from 0.
"""

def sum_of_cubes(array):
  total = 0
  for i in range(len(array)):
    if (i + 1) % 3 == 0:
      total -= array[i] ** 3
    else:
      total += array[i] ** 3
  return total