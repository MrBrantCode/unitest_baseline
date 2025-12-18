"""
QUESTION:
Write a function `reverse_string(s)` that takes a string `s` as input and returns the string in reverse order. The function should use a constant amount of extra space and have a time complexity of O(n), where n is the length of the string.
"""

def reverse_string(s):
    # Convert the string to a list of characters
    chars = list(s)
    
    # Get the length of the string
    n = len(s)
    
    # Swap characters from the beginning and end of the list until reaching the middle
    for i in range(n // 2):
        chars[i], chars[n - i - 1] = chars[n - i - 1], chars[i]
    
    # Convert the list of characters back to a string and return it
    return ''.join(chars)