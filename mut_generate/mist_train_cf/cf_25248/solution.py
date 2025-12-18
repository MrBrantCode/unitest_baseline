"""
QUESTION:
Write a function `permute(string)` that generates all possible permutations of the input string without using any built-in permutation functions. The function should return a list of all unique permutations. The input string may contain repeated characters, but the output should not contain any duplicate permutations.
"""

def permute(string):
  """
  Generates all possible permutations of the input string without using any built-in permutation functions.

  Args:
    string (str): The input string.

  Returns:
    list: A list of all unique permutations of the input string.
  """
  # base case
  if len(string) == 1:
    return [string]

  results = set()
  # iterate through each character in the string
  for i in range(len(string)):
    # select the ith character
    char = string[i]
    # generate all the permutations from the remaining characters
    remaining_characters = string[:i] + string[i+1:]
    permutations = permute(remaining_characters)
    # append the ith character to the beginning of each permutation and add to the result set
    for permutation in permutations:
      results.add(char + permutation)

  return list(results)