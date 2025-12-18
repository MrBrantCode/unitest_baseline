"""
QUESTION:
Create a function `to_camel_case(s)` that converts any given textual string `s` into a camelCase representation. The function should handle special characters by removing them, treat multiple spaces as a single space, and maintain the original case for non-ASCII characters. The function should also handle multilingual inputs. The time complexity of the solution should be optimal.
"""

import re

def to_camel_case(s):
    # Remove all special characters
    s = re.sub(r'\W', ' ', s)
    
    # Convert multiple spaces into a single space
    s = re.sub(r'\s+', ' ', s)
    
    # Split the string into words
    words = s.split(' ')
    
    # Concatenate all words into a string, capitalizing the first letter of each word except the first word
    words = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    
    return ''.join(words)