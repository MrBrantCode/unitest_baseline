"""
QUESTION:
Construct a function named `charCount` that takes a string input and returns a dictionary. The dictionary should contain the count of each unique alphabetical character in the input string, with the counts being case-insensitive (i.e., 'a' and 'A' are considered the same). The function should ignore non-alphabetical characters and be optimized for performance to handle large input strings.
"""

from collections import defaultdict

def charCount(input_string):
  countDict = defaultdict(int)
  for i in input_string:
    if i.isalpha():
        countDict[i.lower()] += 1
  return countDict