"""
QUESTION:
Design a function named `validate_string` that takes a string `text` as input and returns `True` if the string contains at least 2 but no more than 10 punctuation marks, and `False` otherwise. The function should consider commas, periods, exclamation points, question marks, colons, and semi-colons as punctuation marks.
"""

import re
import string

def validate_string(text):
    # Use regex to find all punctuation marks using string.punctuation 
    punctuation_marks = re.findall(r'[' + re.escape(string.punctuation) + ']', text)
  
    # Return True if between 2 and 10 marks, False otherwise
    return 2 <= len(punctuation_marks) <= 10