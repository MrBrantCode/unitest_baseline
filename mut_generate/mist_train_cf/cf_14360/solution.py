"""
QUESTION:
Write a function `unique_characters(strings)` that takes a list of strings as input and returns a string containing all unique characters from the input strings. The function should have a time complexity of O(N) and a space complexity of O(N), where N is the total number of characters in all the strings combined.
"""

def unique_characters(strings):
    # Create a set to store unique characters
    unique_chars = set()
    
    # Iterate over each string in the input list
    for string in strings:
        # Iterate over each character in the string
        for char in string:
            # Add the character to the set
            unique_chars.add(char)
    
    # Convert the set to a string and return it
    return ''.join(unique_chars)