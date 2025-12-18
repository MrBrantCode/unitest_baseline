"""
QUESTION:
Write a function called `delete_occurrences` that takes a string and a character as input and returns a new string with all occurrences of the given character removed, ignoring the case of the characters in the string.
"""

def delete_occurrences(string, char):
    # Convert the given character to lowercase
    char = char.lower()
    
    # Initialize an empty string to store the modified string
    modified_string = ""
    
    # Iterate over each character in the string
    i = 0
    while i < len(string):
        # Convert the current character to lowercase
        current_char = string[i].lower()
        
        # Check if the current character is equal to the given character
        if current_char == char:
            # If so, move to the next character without adding it to the modified string
            i += 1
        else:
            # If not, add the current character to the modified string
            modified_string += string[i]
            i += 1
    
    return modified_string