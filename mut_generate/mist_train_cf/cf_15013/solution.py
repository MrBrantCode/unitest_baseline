"""
QUESTION:
Write a function `reverse_words(string)` that takes a string containing only alphabetic characters and spaces as input. The function should reverse the order of words in the string, ignoring any leading or trailing spaces and handling multiple consecutive spaces between words.
"""

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Split the string into words
    words = string.split(" ")
    
    # Reverse the list of words
    words.reverse()
    
    # Join the reversed words with spaces
    reversed_string = " ".join(words)
    
    return reversed_string