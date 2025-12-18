"""
QUESTION:
Create a function `distances` that takes an array of positive and negative decimal numbers as input. The function should calculate the maximum and minimum values in the array without using built-in functions like `min()` and `max()`, and return their indices. Additionally, it should calculate the absolute difference between each element and the maximum value, and between each element and the minimum value, and store these distances in two separate arrays. The function should return these two distance arrays.
"""

def distances(arr):
  # Initialize maximum and minimum values, and their indices
  max_value = arr[0]
  min_value = arr[0]
  max_index = 0
  min_index = 0
  
  # Iterate over the array to find max and min values and their indices
  for i in range(len(arr)):
    if arr[i] > max_value:
      max_value = arr[i]
      max_index = i
    if arr[i] < min_value:
      min_value = arr[i]
      min_index = i

  # Initialize distance arrays
  distances_from_max = [0]*len(arr)
  distances_from_min = [0]*len(arr)

  # Calculate distances from max and min values
  for i in range(len(arr)):
    distances_from_max[i] = abs(arr[i] - max_value)
    distances_from_min[i] = abs(arr[i] - min_value)

  # Return the two distance lists
  return distances_from_max, distances_from_min