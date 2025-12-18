"""
QUESTION:
Create a function named `z_in_middle` that takes a string as input and returns `True` if the character 'z' is present at any position in the string, excluding the first and last characters.
"""

def z_in_middle(s):
   # Check if 'z' is in the string, excluding first and last character
   return 'z' in s[1:-1]