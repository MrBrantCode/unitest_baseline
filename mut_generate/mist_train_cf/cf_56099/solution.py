"""
QUESTION:
Write a function named `convert_to_uppercase` that iterates over each character in a given string. If the character is alphabetic, convert it to uppercase; otherwise, leave it unchanged. The function should return the resulting string.

The function must be able to handle strings containing special characters and should not modify the original string, as strings are immutable in Python.
"""

def convert_to_uppercase(s):
  new_string = ""
  for i in s:
    if i.isalpha():
      new_string += i.upper()
    else:
      new_string += i
  return new_string