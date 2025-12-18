"""
QUESTION:
Write a function `isUnique` that takes a string as input and returns a boolean value indicating whether the string has all unique characters. Assume the character set is ASCII (128 characters) and do not use any additional data structures other than a boolean array.
"""

def isUnique(string):
    # Assuming character set is ASCII (128 characters) 
    if len(string) > 128: 
        return False

    char_set = [False for _ in range(128)] 
    for char in string: 
        char_value = ord(char) 
 
        if char_set[char_value]: 
            return False
 
        char_set[char_value] = True
 
    return True