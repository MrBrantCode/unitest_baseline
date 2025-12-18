"""
QUESTION:
Write a function named `suggest_name` that takes two parameters: `old_var` (the original variable name) and `all_vars` (a set of all existing variable names). The function should generate a new variable name by appending "_suggested" to a sanitized version of `old_var`, replacing any non-alphanumeric characters and ensuring it does not start with a number. If the new variable name already exists in `all_vars`, it should append a numeric suffix and increment it until a unique name is found. Return the new, unique variable name.
"""

import re

def suggest_name(old_var, all_vars):
  sanitized_old_var = re.sub(r'\W|^(?=\d)', '', old_var)
  new_var = sanitized_old_var + "_suggested"
  counter = 1
  while new_var in all_vars:
    new_var = f"{sanitized_old_var}_suggested_{counter}"
    counter += 1
  return new_var