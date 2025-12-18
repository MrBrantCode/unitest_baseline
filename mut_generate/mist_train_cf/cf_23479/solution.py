"""
QUESTION:
Create a function `capitalize_string` that takes a string as input and returns a new string where the first letter of each word is capitalized. The input string may contain multiple words separated by spaces, and the function should preserve the original word order and spacing.
"""

def capitalize_string(string):
    words = string.split(' ')
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)