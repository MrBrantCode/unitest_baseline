"""
QUESTION:
Create a function named `count_words` that takes a string as input and returns the number of words in the string. The function should ignore leading or trailing white spaces and count consecutive white spaces between words as a single word. The function should also handle non-English characters and symbols correctly. The input string should not exceed 100 characters in length. If the string is empty or consists of only white spaces, the function should return 0.
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