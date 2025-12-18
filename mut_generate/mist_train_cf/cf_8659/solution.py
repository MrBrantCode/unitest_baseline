"""
QUESTION:
Create a function 'removeLetters' that takes a string and a letter as input, and returns the string with all instances of the given letter removed. The function must handle both uppercase and lowercase versions of the given letter, preserve the original order of characters, have a time complexity of O(n), and a space complexity of O(1), where n is the length of the string.
"""

def removeLetters(string, letter):
    new_string = ""
    for char in string:
        if char.lower() != letter.lower():
            new_string += char
    return new_string