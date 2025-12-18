"""
QUESTION:
Write a function `find_fruits(text)` that uses regular expressions to extract the words "Apple", "Bananas", and "Oranges" from a given text, ignoring case sensitivity and ensuring the words are matched exactly, not as part of other words.
"""

import re

def find_fruits(text):
  pattern = re.compile(r'\b(apple|bananas|oranges)\b', re.IGNORECASE)
  matches = pattern.findall(text)
  return matches