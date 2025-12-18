"""
QUESTION:
Write a recursive function `uppercase_recursive(statement, index=0)` that converts all alphabetic characters in the input string `statement` to uppercase while preserving the case of non-alphabetic characters, including special characters and punctuation. The function should recursively iterate over each character in the string, updating the case of alphabetic characters and skipping non-alphabetic characters.
"""

def uppercase_recursive(statement, index=0):
    if index == len(statement):
        return statement
    else:
        if statement[index].isalpha():
            return uppercase_recursive(statement[0:index] + statement[index].upper() + statement[index+1:], index+1)
        else:
            return uppercase_recursive(statement, index+1)