"""
QUESTION:
Write a function named `reverse_words` that takes a string containing alphabetic characters and spaces as input. The function should ignore any leading or trailing spaces, handle multiple consecutive spaces between words, and return a string with the words in the input string in reverse order.
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