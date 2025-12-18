"""
QUESTION:
Write a Python function `modified_swap` to perform a modified character rotation on a given string. Rotate characters in blocks of 3, moving the first character of each block to the end of the block and keeping the other two characters in order. The function should use recursion. If the string has less than 4 characters, return the original string without modification.
"""

def modified_swap(given_string):
    # base case 
    if len(given_string) < 4:
      return given_string
    else:
      return given_string[1:3] + given_string[0] + modified_swap(given_string[3:])