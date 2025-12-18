"""
QUESTION:
Create a function `printLetters(string, index)` that prints each letter of the input `string` individually without using any built-in string manipulation functions or loops. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def printLetters(string, index):
    if index >= len(string):
        return
    print(string[index])
    printLetters(string, index + 1)