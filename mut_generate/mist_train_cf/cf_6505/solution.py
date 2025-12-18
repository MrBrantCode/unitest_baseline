"""
QUESTION:
Write a function called `getLengthAndCharacters` that takes a string as input and returns a tuple containing the number of alphanumeric characters in the string and a list of these characters in the order they appear. Alphanumeric characters are defined as any character that is either a letter (uppercase or lowercase) or a digit (0-9).
"""

def getLengthAndCharacters(inputString):
    length = 0
    alphanumericCharacters = []
    
    for char in inputString:
        if char.isalnum():
            length += 1
            alphanumericCharacters.append(char)
    
    return (length, alphanumericCharacters)