"""
QUESTION:
Write a function called `remove_duplicates` that takes a string as input and returns a new string with all duplicate characters removed while preserving the original order of characters. The function should be case-insensitive, treating 'H' and 'h' as the same character. The time complexity of the function should be O(n) and the space complexity should be O(n), where n is the length of the input string.
"""

def remove_duplicates(string):
    # Convert the string to lowercase
    string = string.lower()
    
    # Create an empty dictionary to store unique characters
    unique_chars = {}
    
    # Create an empty list to store the final result
    result = []
    
    # Iterate through each character in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char not in unique_chars:
            # Add the character to the dictionary
            unique_chars[char] = True
            # Add the character to the result list
            result.append(char)
    
    # Convert the list to a string and return the result
    return ''.join(result)