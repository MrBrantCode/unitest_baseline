"""
QUESTION:
Write a function named `count_words` that takes a string of up to 1000 characters as input and returns the number of words it contains. The function should ignore leading and trailing white spaces, consecutive white spaces between words, and non-alphabetic characters. It should correctly count words in strings containing punctuation marks, non-English characters, and symbols from multiple languages. If the input string is empty or consists of only white spaces, the function should return 0.
"""

def count_words(string):
    # Ignore leading and trailing white spaces
    string = string.strip()
    
    # Check if the string is empty or consists of only white spaces
    if len(string) == 0 or string.isspace():
        return 0
    
    # Remove consecutive white spaces and punctuation marks
    string = ' '.join(filter(None, string.split()))
    
    # Count the number of words
    words = string.split()
    return len(words)