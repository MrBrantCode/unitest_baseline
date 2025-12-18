"""
QUESTION:
Create a function called `replace_letters` that takes two parameters: a string `text` and a character `letter`. The function should return a new string where all occurrences of `letter` in `text` are replaced with their corresponding index in `text`.
"""

def replace_letters(text, letter):
  new_text = ""
  for i, char in enumerate(text):
    if char == letter:
       new_text += str(i)
    else:
       new_text += char
  return new_text