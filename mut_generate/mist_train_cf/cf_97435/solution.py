"""
QUESTION:
Write a function `reverse_words` that takes a string of alphabetic characters and spaces as input, and returns a string where the characters within each word are reversed, while maintaining the word order. The function should ignore any leading or trailing spaces and handle multiple consecutive spaces between words.
"""

def reverse_words(string):
    # Remove leading and trailing spaces
    string = string.strip()
    
    # Split the string into a list of words
    words = string.split()
    
    # Reverse the characters within each word
    reversed_words = [word[::-1] for word in words]
    
    # Join the reversed words back together
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string