"""
QUESTION:
Write a Python function `letter_freq(lexemes)` that takes an array of strings `lexemes` as input and returns a dictionary where the keys are unique alphabetical characters from the strings and the values are their corresponding frequency counts. The function should ignore non-alphabetic characters and be case-insensitive.
"""

from collections import defaultdict

def letter_freq(lexemes):
  frequencies = defaultdict(int)
  
  for lexeme in lexemes:
    lexeme = ''.join([char for char in lexeme if char.isalpha()])
    
    for letter in lexeme:
      frequencies[letter.lower()] += 1
  
  return dict(frequencies)