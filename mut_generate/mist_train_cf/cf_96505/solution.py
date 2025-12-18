"""
QUESTION:
Write a function `replace_character` that takes a string as input and returns a string where all occurrences of 'e' are replaced with 'E' if the length of the string is greater than 5, and the original string otherwise. The function should also return the count of occurrences of 'e' in the string, displayed in parentheses after the modified string. The function should be case-sensitive.
"""

def replace_character(string):
    count = string.count('e')
    if len(string) > 5:
        string = string.replace('e', 'E')
    return f"{string} ({count} e)"