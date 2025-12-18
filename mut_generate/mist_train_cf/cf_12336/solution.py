"""
QUESTION:
Implement a function `caesar_cipher(text, shift)` that takes a string `text` and an integer `shift` as input. The function should apply the Caesar Cipher algorithm to `text`, shifting alphabetic characters by `shift` spaces while preserving non-alphabetic characters and maintaining case sensitivity. The shift value can be any integer between -100 and 100. If a shifted character exceeds the limits of the corresponding character set, it should wrap around to the beginning of the character set. Return the encrypted string.
"""

def caesar_cipher(text, shift):
    result = ""
    
    # Loop through each character in the input text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine the character set limits based on the case
            if char.isupper():
                start = ord('A')
                end = ord('Z')
            else:
                start = ord('a')
                end = ord('z')
            
            # Shift the character by the specified number of spaces
            shifted = ord(char) + shift
            
            # Wrap around to the beginning of the character set if necessary
            if shifted > end:
                shifted = start + (shifted - end - 1)
            elif shifted < start:
                shifted = end - (start - shifted - 1)
            
            # Add the shifted character to the result string
            result += chr(shifted)
        else:
            # Add non-letter characters directly to the result string
            result += char
    
    return result