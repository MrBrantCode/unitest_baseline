"""
QUESTION:
Create a function named "math_terms_detector" that uses a regular expression to detect the presence of the mathematical terms "derivative" and "integral" in a given string. The function should return a message indicating whether both, one, or neither of the terms are found in the string.
"""

import re

def math_terms_detector(input_string):
  # Use re.search() to search for the terms in the input_string.
  derivative = re.search('derivative', input_string, re.IGNORECASE)
  integral = re.search('integral', input_string, re.IGNORECASE)

  # Check if "derivative" and/or "integral" found in input_string
  if derivative and integral:
    return "'derivative' and 'integral' found in the string."
  elif derivative:
    return "'derivative' found in the string."
  elif integral:
    return "'integral' found in the string."
  else:
    return "Neither 'derivative' nor 'integral' found in the string."