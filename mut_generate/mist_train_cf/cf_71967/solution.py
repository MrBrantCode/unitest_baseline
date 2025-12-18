"""
QUESTION:
Design a function `contains(arr, target)` that takes two parameters: an array (`arr`) and a target number (`target`). Write an algorithm to detect whether the array contains the given number. The function should return `True` if the array contains the target number, and `False` otherwise.
"""

def contains(arr, target):
  for element in arr:
    if element == target:
      return True
  return False