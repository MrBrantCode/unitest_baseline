"""
QUESTION:
Implement the `caesar_cipher` function that shifts characters in a string by a specified number of spaces. The input string can contain uppercase and lowercase letters, digits, and special characters. The shift value can be any integer between -100 and 100. The output should maintain case sensitivity, preserve special characters or digits, and wrap around character sets if exceeded.
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