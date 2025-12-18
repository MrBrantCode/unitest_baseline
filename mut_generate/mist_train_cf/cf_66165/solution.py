"""
QUESTION:
Implement a function named `purge_and_find` that takes a 2D array of integers as input and returns a cleansed 2D array with all redundant constituents eliminated, along with the highest and lowest unique integer in the entire array that are not duplicated elsewhere. The function should have a time complexity of O(n) to handle large-scale inputs efficiently.
"""

def purge_and_find(arr):
  values = {}
  unique_values = set()

  # Go through each element in the 2D array.
  for subarr in arr:
    for num in subarr:
      # Increment the count in the hash table for every occurrence of a number.
      if num in values:
        values[num] += 1
      else:
        values[num] = 1

  # Construct the list with non-duplicated values & populate unique_values.
  result = []
  for subarr in arr:
    subresult = []
    for num in subarr:
      if values[num] == 1:
        subresult.append(num)
        unique_values.add(num)
    if subresult:  # Add sub-array to result if it is not empty.
      result.append(subresult)

  # Find the maximum and minimum unique value
  max_unique = max(unique_values) if unique_values else None
  min_unique = min(unique_values) if unique_values else None

  return result, max_unique, min_unique