"""
QUESTION:
Write a function named `find_min_index` that takes a list of numbers as input and returns the index of the minimum element. The function should return `None` if the input list is empty.
"""

def find_min_index(lst):
  if len(lst) == 0:
    return None
  min_index = 0
  for i in range(1, len(lst)):
    if lst[i] < lst[min_index]:
      min_index = i
  return min_index