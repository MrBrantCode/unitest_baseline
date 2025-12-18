"""
QUESTION:
Write a function called `reverse_string` that takes a string `s` as input and returns the string with its characters in reverse order. The input string can contain any characters.
"""

def reverse_string(s):
  # initialize an empty string
  reversed_string = ""

  # loop through the string and concatenate the characters in reverse order
  for i in range(len(s) - 1, -1, -1):
    reversed_string += s[i]
  return reversed_string