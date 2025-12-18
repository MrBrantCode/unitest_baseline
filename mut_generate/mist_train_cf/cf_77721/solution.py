"""
QUESTION:
Implement the `find_difference` function to calculate the absolute difference between two integer lists in Python. The function must return a new list where each element is the absolute difference between the corresponding elements from the two input lists. The function should handle cases where the two input lists have different lengths, and it should only consider valid indices, i.e., up to the length of the shorter list.
"""

def find_difference(l1, l2):
  result = []
  for i in range(min(len(l1), len(l2))):
    result.append(abs(l1[i] - l2[i]))
  return result