"""
QUESTION:
Write a function `check_vectors(vector1, vector2)` that takes two distinct numeric vectors as input and returns `False` if no element in `vector1` exists in `vector2`, and `True` otherwise.
"""

def check_vectors(vector1, vector2):
  for i in vector1:
    if i in vector2: 
      return True
  return False