"""
QUESTION:
Write a function called `find_high_low` that takes a list of integers as input and returns the highest and lowest unique integer values in the list. The function should exclude any duplicate values from consideration. The list may be unsorted and may contain arbitrary numbers of duplicate values.
"""

def find_high_low(n_list):
  n_list = list(set(n_list))
  high = n_list[0]
  low = n_list[0]
  for i in n_list:
    if i > high:
      high = i
    elif i < low:
      low = i
  return high, low