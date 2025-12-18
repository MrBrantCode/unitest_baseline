"""
QUESTION:
Implement a function called `reverse_string` that takes a string `s` as input and returns the reversed string. The function should not use any built-in functions or methods that directly reverse the string. It must have a time complexity of O(n), where n is the length of the input string, and should reverse the string in-place without using any additional data structures. The function should handle Unicode characters correctly, preserving the order of individual characters and not altering any combining characters that form a single Unicode character.
"""

def reverse_string(s):
    chars = list(s)
    length = len(s)
    
    for i in range(length // 2):
        chars[i], chars[length - i - 1] = chars[length - i - 1], chars[i]
    
    return ''.join(chars)