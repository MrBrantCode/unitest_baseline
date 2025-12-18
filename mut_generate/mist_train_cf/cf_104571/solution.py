"""
QUESTION:
Write a function `remove_short_words` that takes a string of alphabetical characters and spaces as input, removes all words with less than 5 characters, and returns the modified string with a single space between the remaining words.
"""

def remove_short_words(string: str) -> str:
    # Split the string into a list of words
    words = string.split()
    
    # Iterate through each word in the list
    # and remove words with less than 5 characters
    words = [word for word in words if len(word) >= 5]
    
    # Join the remaining words into a string
    modified_string = ' '.join(words)
    
    return modified_string