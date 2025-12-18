"""
QUESTION:
Write a function named `remove_old_elements` that takes a list of elements as input and returns the list with the oldest elements removed until the list contains at most 10 elements. The oldest elements are the ones at the beginning of the list.
"""

def remove_old_elements(lst):
  for i in range(len(lst) - 10):
    lst.pop(0)
  return lst