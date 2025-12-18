"""
QUESTION:
Implement a function `modify_string(string)` that takes a string as input and returns a new string where the case of each 'o' and 'l' character is swapped, while the rest of the characters remain unchanged. The function should achieve this in O(n) time complexity, where n is the length of the string, and use constant space complexity, without relying on any extra data structures.
"""

def modify_string(string):
    modifiedString = ""
    for char in string:
        if char.lower() == 'o' or char.lower() == 'l':
            if char.islower():
                modifiedString += char.upper()
            else:
                modifiedString += char.lower()
        else:
            modifiedString += char
    return modifiedString