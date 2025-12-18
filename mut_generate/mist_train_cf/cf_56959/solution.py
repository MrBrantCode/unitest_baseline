"""
QUESTION:
Create a function called `reverseString` that takes a string as input and returns the string in reverse order. The function should be able to handle strings of any length. Additionally, create a function called `simpleShiftCipher` that applies a Caesar cipher to a given string with a user-defined shift value. The cipher should only shift alphabetic characters, leaving punctuation and spaces unchanged. The shift value should wrap around the alphabet if necessary. 

The program should also record user information, including their name, the shift value they used, and the timestamp of their interaction, in a log file. The program should prompt the user for their name and the shift value. The original string to be encoded is "Greetings, Universe!".
"""

import datetime
import logging

def reverseString(text):
    reversedText = ''
    for i in range(len(text)-1, -1, -1):
        reversedText += text[i]
    return reversedText

def simpleShiftCipher(text, shift):
    cipherText = ''
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            cipherText += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            cipherText += char
    return cipherText