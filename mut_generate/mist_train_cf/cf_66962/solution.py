"""
QUESTION:
Implement a function called `quick_sort(lst)` that sorts a list of integers in descending order, handles negative numbers and duplicates correctly, and considers time and space complexity.
"""

def quick_sort(lst):
  if len(lst) <= 1:
    return lst
  pivot = lst[len(lst) // 2]
  left = [x for x in lst if x < pivot]
  middle = [x for x in lst if x == pivot]
  right = [x for x in lst if x > pivot]
  return quick_sort(right) + middle + quick_sort(left)