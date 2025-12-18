"""
QUESTION:
Write a function `capitalize_words` that takes a list of strings as input, where each string represents a word. The function should return a new list of strings where the first letter of each word is capitalized and all remaining letters are converted to lowercase. The function should also remove any leading or trailing spaces from each word, and any extra spaces between words should be condensed into a single space. The function should handle cases where words contain special characters or numbers.
"""

import re

def capitalize_words(words):
    capitalized_words = []
    for word in words:
        # Remove leading and trailing spaces
        word = word.strip()
        
        # Replace multiple spaces with a single space
        word = re.sub(' +', ' ', word)
        
        # Capitalize the first letter and convert the rest to lowercase
        word = word.capitalize()
        
        capitalized_words.append(word)
    
    return capitalized_words