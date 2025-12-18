"""
QUESTION:
Create a function `areAnagrams(string1, string2)` that takes two strings as input and returns `True` if they are anagrams of each other, and `False` otherwise. The function should ignore case, whitespace, and special characters when comparing the strings.
"""

def areAnagrams(string1, string2):
  string1 = string1.replace(' ', '').lower()
  string1 = ''.join(e for e in string1 if e.isalnum())
  string2 = string2.replace(' ', '').lower()
  string2 = ''.join(e for e in string2 if e.isalnum())
  return sorted(string1) == sorted(string2)