"""
QUESTION:
Write a function `count_unique_words` that takes a string as input and returns the count of each unique word that starts with a caret (^) symbol and has at least 3 characters. The function should ignore any leading or trailing spaces in the string.
"""

import re

def count_unique_words(string):
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Find all words that start with a caret (^) symbol and have at least 3 characters
    regex = r'\^[\w]{3,}'
    matches = re.findall(regex, string)
    
    # Count the occurrences of each unique word
    word_count = {}
    for word in matches:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count