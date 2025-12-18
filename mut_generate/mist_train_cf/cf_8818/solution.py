"""
QUESTION:
Develop a function `delete_duplicate_characters` that takes a string `string` as input and returns the string with duplicate characters removed and the remaining characters in reverse order. The function should preserve the original order of non-duplicate characters, handle case sensitivity, and support special characters. The input string length is limited to 100 characters. The function must achieve this in O(n) time complexity without using built-in functions or libraries.
"""

def delete_duplicate_characters(s):
    seen = set()
    result = ''
    
    for char in s:
        if char not in seen:
            seen.add(char)
            result += char
    
    return result[::-1]