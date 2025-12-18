"""
QUESTION:
Create a function named `remove_duplicates` that takes a string as an argument. The function should remove all duplicate characters from the string regardless of their adjacency, maintain the order of the remaining characters, and be case-insensitive (i.e., treat uppercase and lowercase characters as duplicates). The function should return the modified string.
"""

def remove_duplicates(string):
    unique_chars = set()
    modified_string = []
    
    # Convert the string to lowercase
    string = string.lower()
    
    # Iterate over each character in the string
    for char in string:
        # Check if the character is already in the set
        if char not in unique_chars:
            # Add the character to the set and append it to the list
            unique_chars.add(char)
            modified_string.append(char)
    
    # Join the characters in the list to form a string
    return ''.join(modified_string)