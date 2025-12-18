"""
QUESTION:
Create a function `hasUniqueCharacters` that determines whether a given string contains all unique characters without using any additional data structures, with a time complexity of O(n). The function should handle strings encoded in ASCII and consider only the characters in the ASCII character set (256 unique characters).
"""

def hasUniqueCharacters(string):
    charSet = [False] * 256

    for ch in string:
        asciiVal = ord(ch)
        if charSet[asciiVal]:
            return False
        charSet[asciiVal] = True

    return True