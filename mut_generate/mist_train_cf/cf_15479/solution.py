"""
QUESTION:
Write a function `reverse_words` that takes a string as input, reverses the order of the words in the string, removes any leading or trailing spaces, and collapses multiple consecutive spaces into a single space. Each word should maintain its original order, but the order of the words in the string should be reversed.
"""

def reverse_words(string):
    # Split the string into words using space as the delimiter
    words = string.split(' ')
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Remove leading and trailing spaces
    reversed_string = ' '.join(reversed_words).strip()
    
    # Collapse multiple consecutive spaces into a single space
    reversed_string = ' '.join(reversed_string.split())
    
    return reversed_string