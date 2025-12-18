"""
QUESTION:
Write a function `check_syntax(code)` that checks if a given string `code` is valid Python syntax. The function should return `True` if the string is valid Python code and `False` otherwise.
"""

import ast

def check_syntax(code):
  try: 
    ast.parse(code) 
  except SyntaxError: 
    return False
  else: 
    return True