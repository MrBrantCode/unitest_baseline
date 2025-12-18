"""
QUESTION:
Create a function called `remove_whitespaces` that takes a string as input. The function should remove any leading and trailing whitespaces from the string, as well as any whitespace characters between words. The resulting string should contain no spaces, with all words concatenated together.
"""

def remove_whitespaces(string):
    # Remove leading and trailing whitespaces
    string = string.strip()
    
    # Remove whitespace characters in between words
    string = ''.join(string.split())
    
    return string