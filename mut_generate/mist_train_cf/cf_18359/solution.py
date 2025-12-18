"""
QUESTION:
Create a function `hasUniqueCharacters` that takes a string as input and returns `True` if all characters in the string are unique, and `False` otherwise. The function should not use any additional data structures other than the input string itself and a fixed-size array of size 256 (to account for ASCII characters). The time complexity of the function should be O(n), where n is the length of the input string.
"""

def hasUniqueCharacters(string):
    charSet = [False] * 256

    for ch in string:
        asciiVal = ord(ch)
        if charSet[asciiVal]:
            return False
        charSet[asciiVal] = True

    return True