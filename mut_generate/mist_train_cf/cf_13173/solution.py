"""
QUESTION:
Write a function `get_top_words` that takes a string as input, and returns the top ten most frequently occurring words in the string, excluding any words that contain numbers or special characters.
"""

import re
from collections import Counter

def get_top_words(string):
    # Remove punctuation and special characters
    cleaned_string = re.sub(r'[^\w\s]', '', string)
    
    # Split string into words
    words = cleaned_string.split()
    
    # Filter out words containing numbers or special characters
    words = [word for word in words if word.isalpha()]
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Get the top ten most frequent words
    top_words = word_count.most_common(10)
    
    return top_words