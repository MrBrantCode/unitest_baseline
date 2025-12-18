"""
QUESTION:
Write a function `check_z_position(word)` that takes a string `word` as input, and returns the index of the character 'z' if it is present in the string (excluding the first and last positions) and is surrounded by vowels on both sides. The function should be case-insensitive. If no such 'z' is found, return -1.
"""

def check_z_position(word):
  word = word.lower()
  for i in range(1, len(word)-1):
    if word[i] == 'z' and word[i-1] in 'aeiou' and word[i+1] in 'aeiou':
      return i
  return -1