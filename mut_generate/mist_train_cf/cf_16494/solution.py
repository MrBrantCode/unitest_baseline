"""
QUESTION:
Design a function `reverse_string_without_vowels_and_duplicates` that takes a string as input and returns a new string with the characters of the original string in reverse order, excluding vowels and duplicates, in a case-insensitive manner.
"""

def reverse_string_without_vowels_and_duplicates(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Create an empty set to store unique characters
    unique_chars = set()
    
    # Create a new string to store the reverse characters
    new_string = ""
    
    # Iterate through each character in the original string
    for char in reversed(string):
        # Ignore vowels
        if char in "aeiou":
            continue
        
        # Ignore duplicate characters
        if char in unique_chars:
            continue
        
        # Add the character to the unique set
        unique_chars.add(char)
        
        # Add the character to the new string
        new_string += char
    
    # Return the new string with reversed characters
    return new_string