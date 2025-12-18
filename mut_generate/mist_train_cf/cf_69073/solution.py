"""
QUESTION:
Create a function called `manipulate_strings` that takes two parameters: `mystrings` (a list of strings) and `indices` (a list of lists of integers). The function should modify the characters at the specified indices in each string to uppercase, preserve the integrity of previous modifications despite new changes, and return the modified strings. Note that the indices are 0-based, meaning the first character in a string is at index 0.
"""

def manipulate_strings(mystrings, indices):
  # Make a copy of input list to not mutate original 
  modified_strings = mystrings[:]

  for i, string in enumerate(mystrings):
    # Convert each string to list to be able to modify characters
    str_list = list(string)
    for j in indices[i]:
      if j < len(str_list):
        # Perform any modification here. For example, changing characters to upper case
        str_list[j] = str_list[j].upper()
    # Join back to make a string and save in modified list
    modified_strings[i] = ''.join(str_list)

  return modified_strings