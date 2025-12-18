"""
QUESTION:
Write a function called `alternate_ascii_code` that takes a string `input_string` as input, replaces every alternate character with its ASCII value, and returns the resulting string. The function should keep characters at even indices unchanged and replace characters at odd indices with their ASCII values.
"""

def alternate_ascii_code(input_string):
  new_string = ''
  
  for i in range(len(input_string)):
    if i%2 == 0:
      new_string += input_string[i]
    else:
      new_string += str(ord(input_string[i]))
      
  return new_string