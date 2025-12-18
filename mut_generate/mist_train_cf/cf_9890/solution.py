"""
QUESTION:
Write a function `reverse_words` that takes a string as input, removes any leading or trailing whitespace, reverses the order of the words, and returns the modified string without altering the position of any punctuation marks within the string.
"""

def reverse_words(string):
    # Remove leading and trailing whitespace
    string = string.strip()
    
    # Split the string into words
    words = string.split()
    
    # Reverse the order of the words
    words = words[::-1]
    
    # Join the words back together with spaces
    reversed_string = ' '.join(words)
    
    return reversed_string