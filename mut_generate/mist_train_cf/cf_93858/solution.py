"""
QUESTION:
Write a function named `reverse_string` that takes an input string and returns its reverse. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(n). The function should be able to handle strings containing Unicode characters, leading or trailing whitespace, empty strings, and strings with multiple consecutive spaces correctly.
"""

def reverse_string(s):
    # convert the string to a list of characters
    s = list(s)
    
    # get the length of the string
    length = len(s)
    
    # reverse the characters in-place
    for i in range(length // 2):
        s[i], s[length - i - 1] = s[length - i - 1], s[i]
    
    # convert the list of characters back to a string
    return ''.join(s)