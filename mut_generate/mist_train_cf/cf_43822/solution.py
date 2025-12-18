"""
QUESTION:
Write a function `sort_nums(lst, order)` that takes a list of integers and a string indicating either 'asc' for ascending or 'desc' for descending, and returns the sorted list. The list should be sorted according to the given order, except for numbers that are multiples of 3, which should be grouped together in their original order at the end of the list. The input list consists of integers only and contains at least one multiple of three.
"""

def sort_nums(lst, order):
  # split the list into multiples of 3 and others
  multiples_of_3 = [num for num in lst if num % 3 == 0]
  others = [num for num in lst if num % 3 != 0]

  # sort the 'others' list in ascending or descending order
  if order == 'asc':
      others = sorted(others)
  else: # 'desc'
      others = sorted(others, reverse=True)

  # append the 'multiples_of_3' list to the 'others' list
  result = others + multiples_of_3
  return result