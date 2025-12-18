"""
QUESTION:
Separate a given string into words and count the number of times each unique word is used, excluding common words and a user-provided list of words to exclude. Common words to exclude by default include "the", "a", "is", "and", "of", and "in". The function should handle hyphenated words and exclude words containing numbers or special characters. Implement the function `separate_and_count_words(string, exclude_words)`, where `string` is the input string and `exclude_words` is a list of words to exclude.
"""

import re
from collections import Counter

def separate_and_count_words(string, exclude_words=[]):
    # Remove special characters and numbers
    string = re.sub('[^a-zA-Z- ]+', '', string)
    
    # Split string into words
    words = string.lower().split()
    
    # Exclude common words and user-defined exclude words
    common_words = ["the", "a", "is", "and", "of", "in"]
    exclude_words = exclude_words + common_words
    words = [word for word in words if word not in exclude_words]
    
    # Split hyphenated words
    words = [word for word in words for word in word.split('-')]
    
    # Count word frequency
    word_count = Counter(words)
    
    return word_count