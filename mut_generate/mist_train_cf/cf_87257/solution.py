"""
QUESTION:
Write a function `reverse_string` that takes a string as input and returns the string with its characters reversed. The function should not use any built-in string reversal functions or libraries. The input string will only contain ASCII characters. The function should have a time complexity of O(n), where n is the length of the string, and should be able to handle large input strings efficiently without causing memory issues.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    chars = list(s)
    
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