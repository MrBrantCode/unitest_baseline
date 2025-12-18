"""
QUESTION:
Create a function named `sort_by_key` that takes two parameters: an array of objects (`arr`) and a key (`key`). The function should return a new array with the objects sorted in ascending order by the value of the specified key. Assume that all objects in the array have the specified key.
"""

def sort_by_key(arr, key):
  """Sorts an array of objects by the specified key in ascending order."""
  return sorted(arr, key=lambda k: k[key])