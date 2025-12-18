"""
QUESTION:
Write a function named `sum` that takes two parameters `a` and `b` and returns their sum if both are integers. If either `a` or `b` is not an integer, the function should return the string "inputs should be numbers". Include error handling for potential exceptions.
"""

def sum(a, b):
    try:
      if isinstance(a, int) and isinstance(b, int):
        return a + b
      else:
        return "inputs should be numbers"
    except Exception: 
        return "inputs should be numbers"
    finally:
        pass