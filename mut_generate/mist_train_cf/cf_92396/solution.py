"""
QUESTION:
Write a function `count_unique_words` that takes a string of space-separated words as input, and returns the count of unique words. The function should be case-insensitive, ignore leading/trailing spaces, and remove punctuation marks and special characters from the words.
"""

def count_unique_words(string):
    # Convert the string to lowercase and remove leading/trailing spaces
    string = string.strip().lower()
    
    # Remove punctuation marks and special characters
    string = ''.join(char for char in string if char.isalnum() or char.isspace())
    
    # Split the string into words
    words = string.split()
    
    # Use a set to store unique words
    unique_words = set(words)
    
    # Return the count of unique words
    return len(unique_words)