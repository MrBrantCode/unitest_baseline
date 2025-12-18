"""
QUESTION:
Write a function `is_palindromic` that takes a multidimensional array of integers as input. The function should return `True` if all sub-arrays in the input array are palindromes after being flattened, and `False` otherwise. A palindrome is a sequence that reads the same backward as forward. The function should handle edge cases such as empty sub-arrays and sub-arrays of different lengths.
"""

def is_palindromic(arrays):
  def flatten(lst):
    result = []
    for sublist in lst:
      if isinstance(sublist, list):
        result.extend(flatten(sublist))
      else:
        result.append(sublist)
    return result

  for array in arrays:
    flat_array = flatten(array)
    if flat_array != flat_array[::-1]:
      return False
  
  return True