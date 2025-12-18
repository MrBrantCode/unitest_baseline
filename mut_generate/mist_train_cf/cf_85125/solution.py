"""
QUESTION:
Design a function `find_strings(array, strings)` that searches for multiple strings in a given 2D array of strings and returns a dictionary containing the coordinates (row and column) of each occurrence of the strings. The function should take a 2D array of strings and a list of search strings as input, and the output dictionary should have the search strings as keys and lists of coordinates as values. The function should return all occurrences of the search strings in the 2D array.
"""

def find_strings(array, strings):
  # Initialize a dictionary to store the results
  result = {string: [] for string in strings}

  # Iterate over the rows
  for i in range(len(array)):
  
    # Iterate over the elements in each row
    for j in range(len(array[i])):

      # Check if the current string matches any of the search strings
      if array[i][j] in strings:

        # Append the coordinates to the corresponding list in the results dictionary
        result[array[i][j]].append([i, j])

  return result