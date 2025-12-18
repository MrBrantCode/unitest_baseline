"""
QUESTION:
Create a function called `count_characters` that takes a string `str1` as input and returns a dictionary where the keys are the characters in the string and the values are their corresponding counts. The function should iterate through each character in the string, incrementing the count in the dictionary if the character already exists, and adding it to the dictionary with a count of 1 if it does not.
"""

def count_characters(str1):
  count = {}
  for i in str1:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  return count