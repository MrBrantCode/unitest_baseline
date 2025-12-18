"""
QUESTION:
Write a function `get_permutations` that generates and returns all possible permutations of a given array. The function should take an array as input and return a list of arrays, where each array is a permutation of the input array.
"""

def get_permutations(array):
  results = []
  if len(array) == 0:
    return results
  if len(array) == 1:
    results.append([array[0]])
    return results
  for i in range(len(array)):
    permutations = get_permutations(array[:i] + array[i+1:])
    for permutation in permutations:
      results.append([array[i]] + permutation)
  return results