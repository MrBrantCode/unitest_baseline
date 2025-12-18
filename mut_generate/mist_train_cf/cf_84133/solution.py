"""
QUESTION:
Create a function named 'encrypt' that takes a string as input and outputs an encrypted string. The function should employ a customized schema to offset the alphabet: all uppercase characters are to be shifted 5 places down, and all lower-case characters are shifted 8 places down, while maintaining case sensitivity and preserving non-alphabetic elements in the final output.
"""

def encrypt(s):
    shift_upper = 5
    shift_lower = 8

    return ''.join([chr((ord(char) - ord('A') + shift_upper) % 26 + ord('A')) if char.isupper() 
                    else chr((ord(char) - ord('a') + shift_lower) % 26 + ord('a')) if char.islower()
                    else char
                    for char in s])