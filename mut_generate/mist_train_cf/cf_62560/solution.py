"""
QUESTION:
Write a function `remove_duplicates` that takes a list `lst` as input and returns a new list with duplicates removed while preserving the original order. The function should also handle nested lists recursively, removing duplicates from them as well. Assume that nested lists contain only immutable types and their order does not matter.
"""

def remove_duplicates(lst):
  new_lst = []
  for item in lst:
    if isinstance(item, list):
      item = remove_duplicates(item)
    if item not in new_lst:
      new_lst.append(item)
  return new_lst