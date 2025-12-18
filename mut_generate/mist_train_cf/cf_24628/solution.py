"""
QUESTION:
Write a function `maxDifference(arr)` that finds the maximum difference between two elements in the array such that the larger element appears after the smaller element. The function takes an array of integers as input and returns the maximum difference. The array may contain duplicate elements and the function should return 0 if the array contains only one element or if the array is empty.
"""

def entrance(arr):
  # Initialize max difference
  max_difference = 0

  # Traverse the array
  for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
      # Find the difference between two elements
      diff = arr[j] - arr[i]

      # Check if the difference is the maximum
      if diff > max_difference:
        max_difference = diff

  return max_difference