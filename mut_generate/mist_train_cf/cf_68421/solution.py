"""
QUESTION:
Create a function `find_sequences_with_a` that uses regular expressions to identify all sequences of alphabetic characters where the letter "a" is present. The function should return all substrings from the input text where the letter 'a' appears, possibly surrounded by other alphabetic characters.
"""

import re

def find_sequences_with_a(text):
   pattern = r'[a-zA-Z]*a[a-zA-Z]*'
   result = re.findall(pattern, text)
   return result