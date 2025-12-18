"""
QUESTION:
Write a function `find_pairs(values)` that takes a list of integers as input and returns all pairs of numbers in the list that sum up to zero. The same number can be used multiple times to form pairs. The function should be optimized to have a time complexity better than O(n^2), where n is the size of the input list.
"""

def find_pairs(values):
  pairs = set()
  paired = {}
  for num in values:
    if -num in paired:
      pairs.add((-num, num))
    paired[num] = True
  return list(pairs)