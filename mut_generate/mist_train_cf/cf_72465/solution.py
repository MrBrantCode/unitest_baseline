"""
QUESTION:
Create a function named `letter_count` that takes a string and an optional list of characters as arguments. The function should return a dictionary with the individual letters or specified characters as keys and their respective counts in the string as values. The function should be case-insensitive, ignoring spaces and considering "H" and "h" as the same. If a character doesn't exist in the string, its count should be 0. The list of characters will be provided in lowercase.
"""

def letter_count(string, characters=None): 
  string = string.lower()
  my_dict = {}
  
  if characters is None: 
    for char in set(string): 
      if char != " ":
          my_dict[char] = string.count(char)
  else: 
    for char in characters: 
      my_dict[char] = string.count(char)
  return my_dict