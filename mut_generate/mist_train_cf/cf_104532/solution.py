"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns the reversed string without using any built-in string manipulation functions or libraries. The function should have a time complexity of O(n), where n is the length of the string.
"""

def entance(s):
    # Convert the string to a list
    s = list(s)
    
    # Get the length of the string
    n = len(s)
    
    # Swap characters from the beginning and end of the string
    for i in range(n // 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
    
    # Convert the list back to a string
    s = ''.join(s)
    
    # Return the reversed string
    return s