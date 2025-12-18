"""
QUESTION:
Implement a function `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions. The function should have a time complexity of O(n) and constant space complexity, where n is the length of the string. It should handle strings with both uppercase and lowercase letters, special characters, spaces, and ignore leading or trailing spaces.
"""

def reverse_string(s):
    # Remove leading and trailing spaces
    s = s.strip()
    
    # Convert string to list of characters
    characters = list(s)
    
    # Get the length of the string
    length = len(characters)
    
    # Reverse the string by swapping characters
    for i in range(length // 2):
        temp = characters[i]
        characters[i] = characters[length - i - 1]
        characters[length - i - 1] = temp
    
    # Convert the list back to a string
    reversed_string = ''.join(characters)
    
    return reversed_string