"""
QUESTION:
Create a function `remove_duplicates` that takes a string as input and returns a string with all duplicate characters removed while maintaining the original order of characters. The input string may contain any printable ASCII characters. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any built-in string manipulation functions or regular expressions.
"""

def remove_duplicates(string):
    # Create a set to store unique characters
    seen = set()

    # Create a list to store the characters in the original order
    result = []

    # Iterate over each character in the string
    for char in string:
        # Check if the character is already in the set
        if char not in seen:
            # Add the character to the set and the result list
            seen.add(char)
            result.append(char)

    # Join the characters in the result list to form the final string
    return ''.join(result)