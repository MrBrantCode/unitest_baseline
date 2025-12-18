"""
QUESTION:
Create a function `find_pair` that takes an array of decimal numbers and a target sum as input. The function should return a pair of numbers from the array whose sum equals the target value. The function should handle cases where the input array is not a list or the target is not a number, and it should be optimized to handle large datasets.
"""

def find_pair(numbers, target):
  if not isinstance(numbers, list) or not isinstance(target, (int, float)):
    return "Input error"

  num_dict = dict()
  for num in numbers:
    if target - num in num_dict:
      return [target-num, num]
    num_dict[num] = None
  return []