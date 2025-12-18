"""
QUESTION:
Transform the input two-dimensional array by multiplying each integer by its 1-based position index in the sub-array and then by 5. The function, `transform_array`, should take a 2D array as input and return the transformed array, considering optimal time and space complexity.
"""

def transform_array(arr):
  return [[num * ind * 5 for ind, num in enumerate(sub, 1)] for sub in arr]