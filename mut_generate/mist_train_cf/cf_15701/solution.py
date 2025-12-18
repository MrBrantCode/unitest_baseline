"""
QUESTION:
Write a function named `reverse_string` that takes a string as input and returns the reversed string. The function must have a time complexity of O(n), where n is the length of the string, and a space complexity of O(n) due to the conversion of the string to a list. The function should handle strings containing Unicode characters, leading or trailing whitespace, empty strings, and multiple consecutive spaces correctly.
"""

def reverse_string(s):
    # convert the string to a list of characters
    s_list = list(s)
    
    # get the length of the string
    length = len(s)
    
    # reverse the characters in-place
    for i in range(length // 2):
        s_list[i], s_list[length - i - 1] = s_list[length - i - 1], s_list[i]
    
    # convert the list of characters back to a string
    return ''.join(s_list)