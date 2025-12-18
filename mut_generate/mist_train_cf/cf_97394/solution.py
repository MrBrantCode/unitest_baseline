"""
QUESTION:
Create a function 'removeLetters' that takes two parameters: a string and a letter, and returns the string with all instances of the given letter removed. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), excluding the space needed for the output string. Do not use any built-in functions or libraries for removing characters from the string.
"""

def removeLetters(string, letter):
    result = ""
    for char in string:
        if char != letter:
            result += char
    return result