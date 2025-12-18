"""
QUESTION:
Implement the `enhance_encode_cyclic` function, which performs cyclic coding on an input string with varying shifts based on the type of input characters, including letters, digits, and punctuation marks. The function should also manage special characters and empty spaces.
"""

def enhance_encode_cyclic(s: str):
    """
    This function performs cyclic coding on input string. The extent of cyclic shifts depends on the type of the input characters like letters, digits, punctuation marks.
    It also handles special characters and empty spaces efficiently.
    
    Parameters:
    s (str): The input string to be encoded
    
    Returns:
    str: The encoded string
    """
    encoded_str = ""
    for char in s:
        if char.isalpha():  # Check if character is a letter
            shift = 3 if char.islower() else 1  # Shift value for lowercase and uppercase letters
            ascii_offset = 97 if char.islower() else 65  # ASCII value of 'a' or 'A'
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        elif char.isdigit():  # Check if character is a digit
            shift = 2  # Shift value for digits
            encoded_char = str((int(char) + shift) % 10)
        elif char.isspace():  # Check if character is a space
            encoded_char = char  # No shift for space
        else:  # For punctuation marks and special characters
            encoded_char = char  # No shift for punctuation marks and special characters
        encoded_str += encoded_char
    return encoded_str