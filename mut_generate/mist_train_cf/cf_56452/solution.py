"""
QUESTION:
Write a function `replace_spaces(s)` that replaces all whitespace characters (including spaces, tabs, newlines, and carriage returns) in the given string `s` with '%20'. The function should remove any leading or trailing whitespace, merge consecutive whitespace characters into a single '%20', preserve the case of letters, and handle Unicode characters.
"""

def replace_spaces(s):
    # Remove leading/trailing spaces and replace other whitespace characters
    s = s.strip().replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    
    # Merge consecutive spaces into a single space
    while '  ' in s:
        s = s.replace('  ', ' ')
    
    # Replace all spaces with '%20'
    s = s.replace(' ', '%20')
    
    return s