"""
QUESTION:
Write a function named 'reverse_string' that takes a string 'user_string' as its parameter and returns the reversed string using recursion. The function should correctly handle the base case where the input string is empty.
"""

def reverse_string(user_string): 
  if len(user_string) == 0: 
    return "" 
  else: 
    return reverse_string(user_string[1:]) + user_string[0]