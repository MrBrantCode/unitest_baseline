"""
QUESTION:
Write a function `extract_unique_chars` that takes a string as input and returns a list of the first and last occurring unique characters in the string, in sorted order. The function should return `None` if there are no unique characters in the string.
"""

def extract_unique_chars(string):
    unique_chars = []
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is unique and hasn't been added to the list yet
        if string.count(char) == 1 and char not in unique_chars:
            unique_chars.append(char)
    
    # Sort the unique characters list
    unique_chars.sort()
    
    # Return the first and last characters
    if unique_chars:
        return [unique_chars[0], unique_chars[-1]]
    else:
        return None