"""
QUESTION:
Write a function `find_missing(A, B)` that takes two sorted integer arrays `A` and `B` of unequal lengths as input and returns two lists. The first list should contain the elements in `B` that are not in `A`, and the second list should contain the elements in `A` that are not in `B`. The arrays can contain both positive and negative numbers. The solution should have a time complexity of O(n).
"""

def find_missing(A, B):
  setA = set(A)
  setB = set(B)
  missing_in_A = setB - setA
  missing_in_B = setA - setB
  return list(missing_in_A), list(missing_in_B)