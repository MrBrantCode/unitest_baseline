"""
QUESTION:
Write a function called `most_frequent_letter` that takes a string as input and returns the most frequent letter in that string. The function should be case-sensitive, meaning it treats uppercase and lowercase letters as distinct characters. The input string can contain any characters, not just letters. If there are multiple letters with the same highest frequency, the function can return any one of them.
"""

from collections import Counter 

def most_frequent_letter(string): 
  # Count the letter frequency 
  words = Counter(string) 
  
  # Identify the most frequent letter 
  most_common = words.most_common(1)[0][0]
  
  # Return the most frequent letter 
  return most_common