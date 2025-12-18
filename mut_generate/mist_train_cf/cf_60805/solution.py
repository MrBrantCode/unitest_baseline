"""
QUESTION:
Create a function `apply_to_second(input_array, g)` that applies a given function `g` to every second element of `input_array`. The function should return the modified array. The input array is 0-indexed, so the first element is considered the first element, not the second. The function `g` is applied to the elements at even indices (1, 3, 5, etc.).
"""

def apply_to_second(input_array, g):
  # List comprehension loops through list, apply g function at every second element
  return [g(x) if i%2 else x for i,x in enumerate(input_array)]