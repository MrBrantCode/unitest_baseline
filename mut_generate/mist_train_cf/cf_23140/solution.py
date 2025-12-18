"""
QUESTION:
Write a function named `reverse_words` that takes a string of alphabetic characters and spaces as input. The function should return the string with all leading and trailing spaces removed, multiple consecutive spaces between words condensed into a single space, and the characters within each word reversed, while maintaining the original word order.
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