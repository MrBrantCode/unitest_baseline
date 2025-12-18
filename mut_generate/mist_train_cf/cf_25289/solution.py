"""
QUESTION:
Create a function called `longest_palindrome` that takes a non-empty string as input and returns its longest palindromic substring.
"""

def longest_palindrome(text):
  longest_palindrome = ""
  for i in range(len(text)):
    for j in range(len(text), i, -1):
      substring = text[i:j]
      if substring == substring[::-1] and len(substring) > len(longest_palindrome):
        longest_palindrome = substring
  return longest_palindrome