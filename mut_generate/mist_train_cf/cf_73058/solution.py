"""
QUESTION:
Write a function named `solve` that takes an array of integers as input and returns a string of the integers sorted in ascending order, with no duplicates, and separated by commas. The function should have a time complexity less than O(n^2).
"""

def solve(arr):
  arr = sorted(set(arr))      # Sorting the array and removing duplicates
  arr = [str(i) for i in arr]  # Converting the integers to string
  return ','.join(arr)        # Creating a single string separated by commas