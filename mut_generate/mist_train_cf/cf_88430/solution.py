"""
QUESTION:
Write a function named `count_unique_words` that takes a string of text as input. The function should return the count of unique words in the string, excluding common stop words like "the", "and", "a", and ignoring case, multiple spaces, and punctuation marks. The solution should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the number of unique words in the string.
"""

import re

def count_unique_words(text):
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Create a set to store unique words
    unique_words = set()
    
    # List of common stop words
    stop_words = set(['the', 'and', 'a'])
    
    # Iterate through the words
    for word in words:
        # Check if the word is not a stop word
        if word not in stop_words:
            # Add the word to the set of unique words
            unique_words.add(word)
    
    # Return the count of unique words
    return len(unique_words)