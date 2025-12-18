"""
QUESTION:
Write a function `is_anagram(s1, s2)` that takes two string inputs and returns a boolean indicating whether they are anagrams of each other, considering letter case as irrelevant and ignoring any spaces. The function should be case-insensitive and able to handle strings containing spaces.
"""

def is_anagram(s1, s2):
  # Remove spaces and convert to lowercase
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()

  # Return boolean value indicating if sorted strings are equal
  return sorted(s1) == sorted(s2)