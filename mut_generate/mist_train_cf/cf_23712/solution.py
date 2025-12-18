"""
QUESTION:
Write a function named `find_non_repeating` that takes an array as input and returns the first non-repeating element in the array. The function should return the first element that appears only once in the array.
"""

def find_non_repeating(array):
  for i in array:
    if array.count(i) == 1:
      return i