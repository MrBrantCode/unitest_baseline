"""
QUESTION:
Write a function `remove_duplicates` that takes a string as input, removes all duplicate characters, and returns the resulting string. The input string may contain any ASCII characters. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any additional data structures. The input string can have a maximum length of 10^6 characters.
"""

def remove_duplicates(string):
    # Convert the string to a list of characters
    chars = list(string)
    
    # Sort the characters in the list
    chars.sort()
    
    # Initialize a pointer to keep track of the last unique character
    last_unique = 0
    
    # Loop through the characters in the list
    for i in range(1, len(chars)):
        # If the current character is different from the last unique character,
        # move the current character to the next unique position in the list
        if chars[i] != chars[last_unique]:
            last_unique += 1
            chars[last_unique] = chars[i]
    
    # Convert the list of characters back to a string
    result = ''.join(chars[:last_unique + 1])
    
    return result