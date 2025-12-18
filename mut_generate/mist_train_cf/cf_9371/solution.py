"""
QUESTION:
Create a function named `count_words` that takes a string as input and returns the number of words in the string. The string may contain punctuation marks and special characters, but the function should ignore these when counting words. The function should also ignore any leading or trailing white spaces and only consider the string if its length is 100 characters or less.
"""

def count_words(string):
    # Remove leading and trailing white spaces
    string = string.strip()

    # Check if the string exceeds the maximum length
    if len(string) > 100:
        return "String exceeds maximum length"

    # Split the string into words using white spaces as delimiters
    words = string.split()

    # Return the number of words
    return len(words)