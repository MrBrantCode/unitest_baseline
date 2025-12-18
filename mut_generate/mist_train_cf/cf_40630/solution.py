"""
QUESTION:
Create a function `most_common_characters(string)` that takes a string as input, ignores spaces, and returns a list of tuples containing the three most common characters and their frequencies in a case-insensitive manner. The function should return the characters in the order of their frequency.
"""

from collections import Counter

def most_common_characters(string):
    # Remove spaces and convert to lowercase
    string = string.replace(' ', '').lower()
    
    # Use Counter to count character frequencies
    char_count = Counter(string)
    
    # Get the three most common characters
    most_common = char_count.most_common(3)
    
    return most_common