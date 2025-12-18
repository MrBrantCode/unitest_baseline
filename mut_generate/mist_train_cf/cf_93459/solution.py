"""
QUESTION:
Create a function `removeLetters` that takes two parameters: `string` and `letter`. The function should return a new string with all instances of `letter` removed from `string`. The time complexity of the function should be O(n) and the space complexity should be O(n), where n is the length of `string`. The function should not use any built-in string removal functions or libraries.
"""

def removeLetters(string, letter):
    result = ""
    for char in string:
        if char != letter:
            result += char
    return result