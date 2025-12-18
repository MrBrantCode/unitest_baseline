"""
QUESTION:
Design a function `replace_non_alphanumeric` that takes a string `inputStr` as input and returns a new string where all non-alphanumeric characters are replaced with '%'. The function should iterate over each character in the input string and append either the original character or '%' to the output string based on whether the character is alphanumeric or not.
"""

def replace_non_alphanumeric(inputStr):
    outputStr = ''
    for character in inputStr:
        if character.isalnum():
            outputStr += character
        else:
            outputStr += '%'
    return outputStr