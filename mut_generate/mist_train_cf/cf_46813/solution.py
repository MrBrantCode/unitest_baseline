"""
QUESTION:
Create a function named `merge_lists` that takes two lists of integers as input. The function should merge the two lists into a single list, remove duplicates, and sort the resulting list in ascending order. The function should return the sorted list. Note that the order of elements in the original lists should not be preserved. The function should work correctly even if the input lists contain duplicate elements.
"""

def merge_lists(list1, list2):
  merged_list = list1 + list2
  merged_list = list(set(merged_list))
  merged_list.sort()
  return merged_list