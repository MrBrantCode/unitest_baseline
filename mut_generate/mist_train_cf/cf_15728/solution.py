"""
QUESTION:
Create a function `count_words` that takes a string of up to 100 characters as input. The function should return the number of words in the string, ignoring leading and trailing white spaces, consecutive white spaces, and non-English characters or symbols. If the string is empty or consists of only white spaces, the function should return 0.
"""

def count_words(string):
    # Remove leading and trailing white spaces
    string = string.strip()
    
    # If the string is empty or consists of only white spaces
    if len(string) == 0:
        return 0
    
    # Split the string into words using white space as the delimiter
    words = string.split()
    
    # Count the number of words
    return len(words)