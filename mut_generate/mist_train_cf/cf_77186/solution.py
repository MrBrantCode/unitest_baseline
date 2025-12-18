"""
QUESTION:
Create a function `calculate` that takes a string argument `exp`, which is a mathematical expression in infix notation, and returns the result of the expression. The function should handle invalid expressions by returning an error message. Implement the function using the `eval` function, but note that this approach can be insecure with untrusted input sources.
"""

def calculate(exp):
  try:
    result = eval(exp)
  except Exception as e:
    return f"Error in expression: {e}"
  return result