"""
QUESTION:
Write a function `char_frequency` that computes the occurrence of each character in a given string, maintaining case sensitivity and considering special characters. The function should return the results in descending order of frequency as a list of tuples, where each tuple contains a character and its frequency.
"""

def char_frequency(s):
  char_dict = {}
  for char in s:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1

  return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)