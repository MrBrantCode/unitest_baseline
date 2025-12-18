"""
QUESTION:
Write a function named `count_unique_words` that takes a string of space-separated words as input, ignores case, punctuation, and special characters, and returns the count of unique words.
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