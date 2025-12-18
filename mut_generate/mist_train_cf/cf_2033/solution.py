"""
QUESTION:
Implement a function named `reverse_string` that takes a string as input and returns the reversed string without using any built-in string reversal functions or libraries. The function should handle strings with special characters and whitespace, preserve the original case of each character, and have a time complexity of O(n), where n is the length of the string. The input string will only contain ASCII characters.
"""

def reverse_string(string):
    # Convert the string to a list of characters
    chars = list(string)
    
    # Define two pointers: start and end
    start = 0
    end = len(chars) - 1
    
    while start < end:
        # Swap the characters at start and end positions
        chars[start], chars[end] = chars[end], chars[start]
        
        # Increment start and decrement end pointers
        start += 1
        end -= 1
    
    # Join the reversed characters and return the result
    return ''.join(chars)