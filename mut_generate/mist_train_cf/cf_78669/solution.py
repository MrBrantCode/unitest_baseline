"""
QUESTION:
Write a function `calc_distance(arr, elem)` that calculates and returns the total distance between all occurrences of a specific element `elem` within a sorted array `arr`. The function should return 0 if there are less than 2 occurrences of the element in the array. The array is guaranteed to be sorted.
"""

def entrance(arr, elem):
  # Get the indices of all occurrences of the element
  indices = [i for i, x in enumerate(arr) if x == elem]
  
  # If there are less than 2 occurrences of the element return 0
  if len(indices) < 2:
    return 0
  
  # Calculate the distance
  dist = 0
  for i in range(1, len(indices)):
    dist += indices[i] - indices[i-1]
  
  return dist