"""
QUESTION:
Write a function `size_of_list` that calculates the total number of elements in a list, including elements in any nested lists, regardless of their depth. The function should take one argument, `my_list`, which is the list to be processed. The function should return the total count of elements in the list.
"""

def size_of_list(my_list):
  size = 0
  for item in my_list:
    if isinstance(item, list):
      size += size_of_list(item)
    else:
      size += 1
  return size