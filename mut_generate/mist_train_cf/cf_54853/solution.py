"""
QUESTION:
Write a recursive function named `reverse_string` that takes a string `s` as an argument and returns the reversed string without using any built-in functions, methods, or loops. The function should be able to handle both regular and unicode characters.
"""

def reverse_string(s):
   if len(s) == 0:
       return s
   else:
       return reverse_string(s[1:]) + s[0]