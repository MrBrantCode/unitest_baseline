"""
QUESTION:
Write a function `count_lists` that takes a list of lists as input. The function should count the number of unique elements in each sublist and return a dictionary where the keys are the indices of the sublists and the values are dictionaries containing the unique elements of the sublist as keys and their counts as values. The function should only process elements that are lists.
"""

def count_lists(l):
  result = {}
  for i, sublist in enumerate(l):
    if type(sublist) == list:
      inner_dict = {}
      for item in sublist:
        if item in inner_dict:
          inner_dict[item] += 1
        else:
          inner_dict[item] = 1
      result[i] = inner_dict
  return result