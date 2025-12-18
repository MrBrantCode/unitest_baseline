"""
QUESTION:
Design a function named `find_first_and_last` to find the indices of the first and last occurrence of a target value within a sorted array in descending order. The function should take two parameters: a list `lst` containing distinct elements and a target value `target`. The function should return a pair of indices for the first and last occurrences of the target, or (-1, -1) if the target does not exist in the list. Note that the indexing should start at 0.
"""

def find_first_and_last(lst, target):
  first = -1
  last = -1
  for i in range(0, len(lst)):
    if lst[i] == target:
      if first == -1:
        first = i
      last = i
  return (first, last)