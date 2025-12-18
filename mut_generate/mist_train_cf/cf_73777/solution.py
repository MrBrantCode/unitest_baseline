"""
QUESTION:
Create a function `find_substrings` that takes in a list of strings `string_list` and a substring `sub_string` as input. The function should return a list of all strings from `string_list` that contain `sub_string`, ignoring case sensitivity and handling overlapping instances. If no matches are found, the function should return 'No matches found.'
"""

def find_substrings(string_list, sub_string):
  """Returns a list of all strings from `string_list` that contain `sub_string`, 
  ignoring case sensitivity and handling overlapping instances. If no matches are found, 
  returns 'No matches found.'"""
  
  # Empty list to store matched strings
  matches = []

  # loop through string_list
  for string in string_list:
    # Using the lower() function to ignore case sensitivity
    if sub_string.lower() in string.lower():
      matches.append(string)

  # Check if matches list is empty
  if not matches:
    return 'No matches found.'
  else:
    return matches