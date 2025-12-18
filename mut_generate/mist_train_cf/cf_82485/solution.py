"""
QUESTION:
Implement a function `exponential_diff(l: list, k: int, x: int, strict: bool = False)` that checks if the difference between every two successive elements in the list `l` is `k` raised to the power of `x`. If `strict` is `True`, no two adjacent elements can be the same; otherwise, they can be. The function should return `True` only when the difference condition is met for all elements and the strictness condition is satisfied if applicable.
"""

def exponential_diff(l: list, k: int, x: int, strict: bool = False) -> bool:
  """
  Check if the difference between every two successive elements 
  in the list is the k'th power of x. 
  If the option 'strict' is True, no two neighboring elements can be the same; 
  otherwise, they can be. 
  The function returns True only when the difference between every two 
  successive elements is k raised to the power of x.

  """
  last = l[0]
  for el in l[1:]:
    if strict and el == last:
      return False
    if el - last != k ** x:
      return False
    last = el
  return True