"""
QUESTION:
Create a function called `remove_whitespaces` that takes a string as input and returns a string with all leading, trailing, and in-between whitespace characters removed.
"""

def remove_whitespaces(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Remove whitespace characters in between words
    string = ''.join(string.split())
    
    return string