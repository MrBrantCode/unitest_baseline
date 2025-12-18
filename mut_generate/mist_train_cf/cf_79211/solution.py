"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` is a palindrome without using any built-in string methods or functions. The function should return `True` if the string is a palindrome and `False` otherwise.
"""

def is_palindrome(s):
   length = 0

   # Get the length of the string
   for i in s:
      length += 1

   # Compare the characters from both ends
   for i in range(length // 2):
      if s[i] != s[length - i - 1]:
         return False

   return True