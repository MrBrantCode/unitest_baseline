"""
QUESTION:
Implement a function `testing` that takes a string as input. The function should check if the input string contains only alphabetic characters. If it does, convert all lowercase letters to uppercase and all uppercase letters to lowercase. If it does not, return an error message. The function should return the modified string if the input string is valid.
"""

def testing(myString):
    if myString.isalpha():  
        modified_string = myString.swapcase()  
        return modified_string
    else:
        return "Input string should contain only alphabetic characters"