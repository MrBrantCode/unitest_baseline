"""
QUESTION:
Write a function `longest_common_prefix` that takes an array of strings as input and returns the longest common prefix of all the strings in the array. If the array is empty, the function should return an empty string.
"""

def longest_common_prefix(array):
  if len(array) == 0:
    return ""

  # sort the array
  array.sort()

  # compare the first and last word in sorted array
  first_word = array[0]
  last_word = array[-1]
  
  i = 0
  # iterate through every character in the first_word
  for i in range(min(len(first_word), len(last_word))):
    # if characters match, continue
    # if characters do not match, break the loop
    if first_word[i] != last_word[i]:
      break

  # slice the first_word up to the matching index to get the prefix
  return first_word[:i]